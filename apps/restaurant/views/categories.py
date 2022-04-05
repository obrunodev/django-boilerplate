from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from restaurant.models import Category


def categories_index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'categories/pages/index.html', context)


def categories_create(request):
    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            messages.error(request, 'Algo deu errado!')
            return redirect('restaurant:categories_index')

        category = Category.objects.create(name=name)
        messages.success(request, f'Nova categoria "{category}" cadastrada!')
        return redirect('restaurant:categories_index')


def categories_update(request, category_id):
    ...


def categories_delete(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=category_id)
        category.delete()
        messages.success(request, f'Categoria "{category}" removida!')
        return redirect('restaurant:categories_index')
