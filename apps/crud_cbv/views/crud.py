from django.shortcuts import render


def index(request):
    return render(request, 'crud_cbv/pages/index.html')
