from django import forms
from django.forms import DateInput

from .models import Author, Book

class AuthorCreateForm(forms.ModelForm):
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
    
    def clean_age(self):
        age = self.cleaned_data['age']
        if int(age) > 102:
            self.add_error('age', 'The oldest author till date was 102 years old, please enter an age < 102')
        elif int(age) <= 5:
            self.add_error('age', 'The youngest author till date is 5 years old, please enter an age > 5')
        return age
    
class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'date_of_publishing': forms.DateInput(attrs={
                'type': 'date'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super(BookCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
