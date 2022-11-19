import django_filters
from .models import Author

class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Author
        fields = ['age', 'gender', 'name']