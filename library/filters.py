from datetime import datetime
import django_filters
from django_filters import RangeFilter, DateRangeFilter
from django_filters.widgets import RangeWidget
from django_filters.fields import RangeField
from django.forms import DateField, IntegerField
from django.forms.widgets import TextInput, Select, NumberInput

from .models import Author, Book, Country, Author

# Filters
class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', 
        label='Author Name', 
        lookup_expr='icontains', 
        widget=TextInput(attrs={
            'class': 'form-control'
        }))
    gender = django_filters.ChoiceFilter(
        field_name='gender', 
        label='Gender',
        choices=Author.GENDER_CHOICES,
        widget=Select(attrs={
            'class': 'form-select'
        }))
    age = django_filters.NumberFilter(
        field_name='age', 
        label='Age',
        widget=NumberInput(attrs={
            'class': 'form-control'
        }))
    class Meta:
        model = Author
        fields = ['age', 'gender', 'name']

class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', 
        label='Book Name', 
        lookup_expr='icontains', 
        widget=TextInput(attrs={
            'class': 'form-control'
        }))
    min_avg_critics_rating = django_filters.NumberFilter(
        field_name='average_critics_rating', 
        label='Min. Avg. Ratings',
        lookup_expr='gte',
        widget=Select(
            choices=((i, i) for i in range(0, 11)),
            attrs={
                'class': 'form-select'
            }
        ))
    page_range = django_filters.RangeFilter(
        field_name='number_of_pages',
        widget=RangeWidget(attrs={
            'class': 'form-control'
        })
    )
    min_published_year = django_filters.CharFilter(
        field_name='date_of_publishing',
        label='Publish Date Between',
        method='find_books_published_after',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Published After'
        })
    )
    max_published_year = django_filters.CharFilter(
        field_name='date_of_publishing',
        label='Publish Date Between',
        method='find_books_published_before',
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Published Before'
        })
    )
    class Meta:
        model = Book
        fields = ['name', 'min_avg_critics_rating', 'page_range', 'min_published_year', 'max_published_year']
    
    def find_books_published_after(self, queryset, name, value):
        value = datetime(int(value), 1, 1)
        return queryset.filter(**{
            f"{name}__gte": value
        })

    def find_books_published_before(self, queryset, name, value):
        value = datetime(int(value), 1, 1)
        return queryset.filter(**{
            f"{name}__lte": value
        })