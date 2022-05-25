from django.shortcuts import render

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        pass
    else:
        context = {'form': RegisterForm()}
        return render(request, 'users/pages/register.html', context)


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'users/pages/login.html')
