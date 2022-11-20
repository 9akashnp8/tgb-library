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
    
    def __init__(self, *args, **kwargs):
        super(AuthorCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == "gender" or field == "country":
                self.fields[field].widget.attrs.update({'class': 'form-select'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
    
class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(BookCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == "author":
                self.fields[field].widget.attrs.update({'class': 'form-select'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
