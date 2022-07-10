from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@login_required(login_url='user:signin')
def profile(request):
    return render(request, 'user/pages/profile.html')


def signin(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            account = User.objects.get(email=email)
            user = auth.authenticate(username=account.username, password=password)

            if not email or not password:
                messages.success(request, "Precisa preencher todos os campos!")
                return redirect('user:signin')

            if user is not None:
                auth.login(request, user)
                messages.success(request, "Logado com sucesso")
                return redirect('user:profile')

            messages.error(request, "Não foi possível logar. Tente novamente!")
            return redirect('user:signin')
        
        except User.DoesNotExist:
            messages.success(request, "Este e-mail não existe! Crie uma conta para ter acesso.")
            return redirect('user:signin')
    
    if request.method == 'GET':
        return render(request, 'user/pages/signin.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not email or not username or not password:
            messages.error(request, 'Preencha todos os campos!')
            return redirect('user:signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado!')
            return redirect('user:signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já cadastrado!')
            return redirect('user:signup')

        if password != password2:
            messages.error(request, 'Senhas não batem!')
            return redirect('user:signup')

        user = User.objects.create_user(username, email, password)
        auth.login(request, user)
        messages.success(request, 'Cadastrado com sucesso!')
        return redirect('user:profile')
    
    if request.method == 'GET':
        return render(request, 'user/pages/signup.html')


def logout(request):
    auth.logout(request)
    return redirect('user:signin')
