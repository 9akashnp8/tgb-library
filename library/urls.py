from django.urls import path
from .views import Home, AuthorListView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('author/', AuthorListView.as_view(), name='author_list'),
]