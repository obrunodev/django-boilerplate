from django.shortcuts import redirect, render, get_object_or_404

from crud.models import Book

from crud.forms import BookForm


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'books/pages/index.html', context)


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'books/pages/detail.html', context)


def new(request):
    return render(request, 'books/pages/new.html')


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            book_obj = form.save(commit=False)
            book_obj.slug = str(book_obj.title).replace(' ', '-').lower()
            book_obj.save()
            return redirect('crud:books_index')
        return redirect('crud:books_index')


def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST or None, instance=book)
        if form.is_valid():
            book_obj = form.save(commit=False)
            book_obj.slug = str(book_obj.title).replace(' ', '-').lower()
            book_obj.save()
            return redirect('crud:books_index')
        return redirect('crud:books_index')


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('crud:books_index')
