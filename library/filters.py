import django_filters
from .models import Author

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ['age', 'gender', 'name']