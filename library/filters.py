from datetime import datetime
import django_filters
from django_filters.widgets import RangeWidget
from django.forms.widgets import DateInput, TextInput, Select, NumberInput

from .models import Author, Book, Country, Author

# Extensions/Customizations
class CustomRangeWidget(RangeWidget):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        widgets = (TextInput(attrs={
            'placeholder': 'Hello'
        }), TextInput)

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
        lookup_expr='gt',
        widget=Select(
            choices=((i, i) for i in range(0, 11)),
            attrs={
                'class': 'form-select'
            }
        ))
    page_range = django_filters.RangeFilter(
        field_name='number_of_pages',
        widget=CustomRangeWidget(attrs={
            'class': 'form-control'
        })
    )
    published_year = django_filters.DateRangeFilter(
        field_name='date_of_publishing',
        label='Year of Publishing',
        widget=Select(attrs={
            'class': 'form-select'
        })
    )
    class Meta:
        model = Book
        fields = ['name', 'min_avg_critics_rating', 'page_range', 'published_year']