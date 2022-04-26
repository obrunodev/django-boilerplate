from django import forms

from .models import Product
from .models import Purchase


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'price',
                  'quantity',
                  'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.TextInput(attrs={'class': 'input'}),
            'price': forms.TextInput(attrs={'class': 'input'}),
            'quantity': forms.TextInput(attrs={'class': 'input'}),
            'category': forms.Select(attrs={'class': 'select'}),
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product',
                  'quantity',
                  'cost']
