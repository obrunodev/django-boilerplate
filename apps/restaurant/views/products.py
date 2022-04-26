from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from restaurant.models import Product
from restaurant.models import Category

from restaurant.forms import ProductForm


def products_index(request):
    context = {
        'form': ProductForm(),
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
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
        category = request.POST['category']
        form = ProductForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.slug = obj.name.replace(' ', '-').lower()
            obj.save()
            messages.success(request, f'Produto " {obj.name} " cadastrado com sucesso!')
            return redirect('restaurant:products_index')
        print(form.errors)
        return redirect('restaurant:products_index')


def products_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('restaurant:products_index')
    print(form.errors)
    return redirect('restaurant:products_index')


def products_delete(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('restaurant:products_index')
