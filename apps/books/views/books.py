from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book
from books.forms import BookForm


def index(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/pages/index.html', {'page_obj': page_obj})


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('books_index')
        messages.error(request, 'Não foi possível cadastrar o livro!')
        return redirect('books_index')
    else:
        return render(request, 'books/pages/create.html')


def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('books_index')
        messages.error(request, 'Não foi possível atualizar o livro!')
        return redirect('books_index')
    else:
        context = {'book': book}
        return render(request, 'books/pages/update.html', context)


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Livro removido com sucesso')
        return redirect('books_index')
    else:
        context = {'book': book}
        return render(request, 'books/pages/delete.html', context)


def index_view(request):
    return render(request, 'books/pages/vue.html')


def index_json(request):
    books = Book.objects.values()
    return JsonResponse({'response': list(books)})
