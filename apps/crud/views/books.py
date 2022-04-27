from django.shortcuts import render

from crud.models import Book


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'books/pages/index.html', context)


def detail(request):
    pass


def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass
