from django.contrib import messages
from django.shortcuts import render, redirect

from restaurant.models import Product
from restaurant.models import Purchase


def purchase_index(request):
    context = {
        'products': Product.objects.all(),
        'purchases': Purchase.objects.all(),
    }
    return render(request, 'purchases/pages/index.html', context)


def purchase_create(request):
    if request.method == 'POST':
        product = request.POST['product']
        quantity = request.POST['quantity']
        cost = request.POST['cost']
        total_cost = float(cost) * int(quantity)

        if not product or not quantity or not cost:
            messages.error(request, 'Todos os campos precisam estar preenchidos!')
            return redirect('restaurant:purchases_index')

        Purchase.objects.create(product=Product.objects.get(name=product),
                                quantity=quantity,
                                cost=cost,
                                total_cost=total_cost)
        product_obj = Product.objects.get(name=product)
        product_obj.quantity = int(product_obj.quantity) + int(quantity)
        product_obj.save()
        messages.success(request, 'Compra registrada com sucesso!')
        return redirect('restaurant:purchases_index')
