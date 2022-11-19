from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Author, Book
from .forms import AuthorCreateForm, BookCreateForm
from .filters import AuthorFilter, BookFilter
from .resources import AuthorResource, BookResource

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
    return render(request, 'author/book_list.html', context)

# Helpers
def export_author(request):
    author_resource = AuthorResource()
    dataset = author_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="authors.csv"'
    return response

def export_book(request):
    author_resource = BookResource()
    dataset = author_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="books.csv"'
    return response

# HTMX Helpers
def authors_list(request):
    filter = AuthorFilter(request.GET, queryset=Author.objects.all())
    context = { 'filter': filter}
    return render(request, 'partials/author_filtered_result.html', context)

def books_list(request):
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = { 'filter': filter}
    return render(request, 'partials/author_filtered_result.html', context)