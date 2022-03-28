from django.shortcuts import render, redirect, get_object_or_404

from products.forms import ProductForm
from products.models import Product


def products_index(request):
    context = {
        'form': ProductForm(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/pages/index.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'form': ProductForm(instance=product),
        'product': product,
    }
    return render(request, 'products/pages/detail.html', context)


def products_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('products:index')
        print(form.errors)
        return redirect('products:index')


def products_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products:index')
    print(form.errors)
    return redirect('products:index')


def products_delete(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('products:index')
