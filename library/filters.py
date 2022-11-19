import django_filters
from django.forms.widgets import DateInput, TextInput
from .models import Author, Book

# Filters
class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', 
        label='Author Name', 
        lookup_expr='icontains', 
        widget=TextInput(attrs={
            'hx-get': '/htmx/author/filter',
            'hx-trigger': 'change',
            'hx-params': '*',
            'hx-target': '#result',
        }))

    class Meta:
        model = Author
        fields = ['age', 'gender', 'name']

class BookFilter(django_filters.FilterSet):
    min_avg_critics_rating = django_filters.NumberFilter(field_name='average_critics_rating', lookup_expr='gt')
    min_page = django_filters.NumberFilter(field_name='number_of_pages', lookup_expr='gte')
    max_page = django_filters.NumberFilter(field_name='number_of_pages', lookup_expr='lte')
    min_published_year = django_filters.DateFilter(
        field_name='date_of_publishing', 
        lookup_expr='gte', 
        widget=DateInput(attrs={'type': 'date'})
    )
    max_published_year = django_filters.DateFilter(
        field_name='date_of_publishing', 
        lookup_expr='lte',
        widget=DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Book
        fields = ['name', 'min_avg_critics_rating', 'min_page', 'max_page', 'min_published_year', 'max_published_year']