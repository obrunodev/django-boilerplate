from django.shortcuts import redirect, render

from crud_fbv.models import Book
from crud_fbv.models import Genre
from crud_fbv.forms import BookForm
from crud_fbv.forms import GenreForm


def index(request):
    books = Book.objects.all()
    return render(request, 'crud_fbv/pages/index.html', {'books': books})


def create(request):
    context = {}

    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('crud_fbv:index')
        context['form'] = form

    if request.method == 'GET':
        context['form'] = BookForm()
    
    context['genres'] = Genre.objects.all()
    
    return render(request, 'crud_fbv/pages/create.html', context)


def update(request, pk):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass


def delete(request, pk):
    if request.method == 'POST':
        pass

    if request.method == 'GET':
        pass
