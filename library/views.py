from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Author
from .forms import AuthorCreateForm
from .filters import AuthorFilter

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

# class AuthorListView(ListView):
#     model = Author
#     template_name = 'author/author_list.html'

def author_list_and_create_view(request):
    filter = AuthorFilter(request.GET, queryset=Author.objects.all())
    form = AuthorCreateForm()
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, f'{instance.name} Successfuly Added as an Author.')
            return redirect('/author/')
    context = {'form': form, 'filter': filter}
    return render(request, 'author/author_list.html', context)