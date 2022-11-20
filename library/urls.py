from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'author', views.AuthorViewSet, basename='author')
router.register(r'book', views.BookViewSet, basename='book')

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('author/', views.author_list_and_create_view, name='author_list'),
    path('author/export/', views.export_author, name='author_export'),
    path('author/import/', views.import_author, name='author_import'),
    path('book/', views.book_list_and_create_view, name='book_list'),
    path('book/export/', views.export_book, name='book_export'),
    path('book/import/', views.import_book, name='book_import'),


    # HTMX
    path('htmx/author/filter', views.authors_list, name='author-filter'),
    path('htmx/book/filter', views.books_list, name='book-filter'),
    path('api/', include(router.urls)),
]