from django.contrib import admin

from .models import Country, Author, Book

# Register your models here.
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Book)