from django import forms
from django.forms import DateInput

from .models import Author, Book

class AuthorCreateForm(forms.ModelForm):
    widgets = {
        'date_of_publishing': DateInput(attrs={'type': 'date'})
    }

    class Meta:
        model = Author
        fields = '__all__'
    
class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
