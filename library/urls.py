from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('author/', views.author_list_and_create_view, name='author_list'),
    path('author/export/', views.export_author, name='author_export'),
    path('book/', views.book_list_and_create_view, name='book_list'),

    # HTMX
    path('htmx/author/filter', views.authors_list, name='author-filter'),
    path('htmx/book/filter', views.books_list, name='book-filter'),
]