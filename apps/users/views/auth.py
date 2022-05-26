from django.contrib import messages
from django.shortcuts import render, redirect

from ..forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.sucess(request, 'Conta criada com sucesso!')
            return redirect('users:register')
        messages.error(request, 'Não foi possível criar uma conta, tente novamente!')
        return redirect('users:register')
    else:
        context = {'form': RegisterForm()}
        return render(request, 'users/pages/register.html', context)


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'users/pages/login.html')
