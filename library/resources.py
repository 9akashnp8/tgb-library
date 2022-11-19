from import_export import resources
from .models import Author

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author