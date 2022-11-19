from django.urls import path
from .views import Home, author_list_and_create_view, authors_list

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('author/', author_list_and_create_view, name='author_list'),

    # HTMX
    path('htmx/author/filter', authors_list, name='author-filter'),
]