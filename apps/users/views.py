from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'users/pages/register.html')


def login(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'users/pages/login.html')
