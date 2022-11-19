from import_export import resources
from .models import Author, Book

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class BookResource(resources.ModelResource):
    class Meta:
        model = Book