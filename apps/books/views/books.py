from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book
from books.forms import BookForm


def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books/pages/index.html', context)


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_create')
        print(form.errors)
        return redirect('books_create')
    else:
        return render(request, 'books/pages/create.html')


def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_index')
        return redirect('books_index')
    else:
        context = {'book': book}
        return render(request, 'books/pages/update.html', context)


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books_index')
    else:
        context = {'book': book}
        return render(request, 'books/pages/delete.html', context)
