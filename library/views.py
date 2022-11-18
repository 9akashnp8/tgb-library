from django.views.generic import ListView, TemplateView

from .models import Author

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'