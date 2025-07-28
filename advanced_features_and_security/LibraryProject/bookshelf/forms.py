# bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data['title']
        # Additional sanitization if needed
        return title.strip()

    def clean_author(self):
        author = self.cleaned_data['author']
        return author.strip()
