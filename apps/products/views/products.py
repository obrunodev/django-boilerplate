from django.shortcuts import render, redirect

from products.forms import ProductForm
from products.models import Product


def products_index(request):
    context = {
        'form': ProductForm(),
    }
    return render(request, 'products/pages/index.html', context)


def product_detail(request):
    ...


def products_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('products:index')
        print(form.errors)
        return redirect('products:index')


def products_update(request, product_id):
    ...


def products_delete(request, product_id):
    ...
