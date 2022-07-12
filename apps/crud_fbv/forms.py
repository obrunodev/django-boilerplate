from django import forms
from django.core.exceptions import ValidationError

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
        error_messages = {
            'title': {
                'required': 'Este campo é obrigatório.',
                'max_length': 'Este campo não pode ter mais de 100 caracteres.'
            }
        }
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     })
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['genre'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('title') == "":
            name_empty_error = ValidationError(
                'Este campo precisa estar preenchido',
                code='Invalid'
            )
            raise ValidationError({'title': name_empty_error})
