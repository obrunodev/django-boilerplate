from django import forms

from crud_fbv.models import Book
from crud_fbv.models import Genre


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ['name']


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'price']
