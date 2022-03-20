from django.shortcuts import render


def index(request):
    return render(request, 'crud_fbv/pages/index.html')
