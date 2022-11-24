from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import ValidationError

from .models import Author, Book
from .forms import AuthorCreateForm, BookCreateForm
from .filters import AuthorFilter, BookFilter, BookAPIFilter
from .resources import AuthorResource, BookResource
from .serializers import BookSerializer

from tablib import Dataset

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

# class AuthorListView(ListView):
#     model = Author
#     template_name = 'author/author_list.html'

def author_list_and_create_view(request):
    filter = AuthorFilter(request.GET, queryset=None)
    form = AuthorCreateForm()
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, f'{instance.name} Successfuly Added as an Author.')
            return redirect('/author/')
    context = {'form': form, 'filter': filter}
    return render(request, 'author/author_list.html', context)

def book_list_and_create_view(request):
    filter = BookFilter(request.GET, queryset=None)
    form = BookCreateForm()
    if request.method == "POST":
        form = BookCreateForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, f'{instance.name} Successfuly Added as a Book.')
            return redirect('/book/')
    context = {'form': form, 'filter': filter}
    return render(request, 'book/book_list.html', context)

# Helpers
def export_author(request):
    author_resource = AuthorResource()
    dataset = author_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="authors.csv"'
    return response

def import_author(request):
    if request.method == "POST":
        author_resource = AuthorResource()
        dataset = Dataset()
        new_authors = request.FILES.get("authorCSV")

        imported_data = dataset.load(new_authors.read().decode(), format='csv')
        result = author_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            author_resource.import_data(dataset, dry_run=False)
            return redirect('author_list')
    return render(request, 'author/import.html')

def export_book(request):
    book_resource = BookResource()
    dataset = book_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="books.csv"'
    return response

def import_book(request):
    if request.method == "POST":
        book_resource = BookResource()
        dataset = Dataset()
        new_books = request.FILES.get("bookCSV")

        imported_data = dataset.load(new_books.read().decode(), format='csv')
        print(imported_data)
        result = book_resource.import_data(dataset, dry_run=True, raise_errors=True)
        print(result)

        if not result.has_errors():
            book_resource.import_data(dataset, dry_run=False, raise_errors=True)
            return redirect('book_list')
    return render(request, 'book/import.html')

# HTMX Helpers
def authors_list(request):
    filter = AuthorFilter(request.GET, queryset=Author.objects.all())
    context = { 'filter': filter}
    return render(request, 'partials/author_filtered_result.html', context)

def books_list(request):
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = { 'filter': filter}
    if filter.is_valid():
        return render(request, 'partials/book_filtered_result.html', context)
    else:
        return render(request, 'partials/filter_errors.html', context)

# API Views
class BookListView(ListAPIView):
    serializer_class = BookSerializer
    filterset_class = BookAPIFilter

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        if author is not None:
            try:
                a = Author.objects.get(name=author)
                queryset = queryset.filter(author__name=a)
                if len(queryset) == 0:
                    raise ValidationError({
                        'status': 'BookNotFound',
                        'message': f'No Books Found for {a} '
                    })
            except Author.DoesNotExist:
                raise ValidationError({
                    'status': 'AuthorNotFound',
                    'message': f'No Such Author Found, Spell Check the Name or add {author} into our Library.'
                })
        return queryset