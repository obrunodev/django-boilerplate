from django.shortcuts import render, redirect
from django.http import Http404

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        return redirect('users:register')
    else:
        context = {'form': RegisterForm()}
        return render(request, 'users/pages/register.html', context)


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'users/pages/login.html')
