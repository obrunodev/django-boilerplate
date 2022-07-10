from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.forms import SignInForm
from user.forms import SignUpForm


@login_required(login_url='user:signin')
def profile(request):
    return render(request, 'user/pages/profile.html')


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        return
        # try:
        #     email = request.POST['email']
        #     password = request.POST['password']
        #     account = User.objects.get(email=email)
        #     user = authenticate(username=account.username, password=password)

        #     if not email or not password:
        #         messages.success(request, "Precisa preencher todos os campos!")
        #         return redirect('user:signin')

        #     if user is not None:
        #         login(request, user)
        #         messages.success(request, "Logado com sucesso")
        #         return redirect('user:profile')

        #     messages.error(request, "Não foi possível logar. Tente novamente!")
        #     return redirect('user:signin')
        
        # except User.DoesNotExist:
        #     messages.success(request, "Este e-mail não existe! Crie uma conta para ter acesso.")
        #     return redirect('user:signin')
    
    if request.method == 'GET':
        form = SignInForm()
        context = {'form': form}
        return render(request, 'user/pages/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) 
            login(request, user)
            return redirect('user:profile')
        
        context = {'form': form}
        return render(request, 'user/pages/signup.html', context)
    
    if request.method == 'GET':
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'user/pages/signup.html', context)


def signout(request):
    logout(request)
    return redirect('user:signin')
