from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    template_name = 'form_snippet.html'

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password']
