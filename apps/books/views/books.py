from django.shortcuts import render, get_object_or_404

from books.models import Book


def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books/pages/index.html', context)


def create(request):
    pass


def update(request):
    pass


def delete(request):
    pass
