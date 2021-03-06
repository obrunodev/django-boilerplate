from django.shortcuts import get_object_or_404, redirect, render

from crud_fbv.models import Book
from crud_fbv.models import Genre
from crud_fbv.forms import BookForm


# TODO(back-end): Add successes messages
def index(request):
    books = Book.objects.all()
    return render(request, 'crud_fbv/pages/index.html', {'books': books})


def create(request):
    # FIXME(back-end): Permitir valor digitado com vírgula.
    genres = Genre.objects.all()
    context = {'genres': genres}

    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('crud_fbv:index')
        context['form'] = form

    if request.method == 'GET':
        context['form'] = BookForm()
    
    return render(request, 'crud_fbv/pages/create.html', context)


def update(request, pk):
    context = {}
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('crud_fbv:index')

    if request.method == 'GET':
        context['book'] = book
        context['genres'] = Genre.objects.all()

    context['form'] = form
    return render(request, 'crud_fbv/pages/update.html', context)


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('crud_fbv:index')

    return render(request, 'crud_fbv/pages/delete.html', {'book': book})
