from django.shortcuts import render, redirect

from restaurant.models import Sale
from restaurant.models import Cart


def sales_index(request):
    context = {
        'sales': Sale.objects.all(),
    }
    return render(request, 'sales/pages/index.html', context)


def finish_order(request):
    if request.method == 'POST':
        cart = Cart.objects.all()
        total = 0
        for item in cart:
            total += item.product.price
        Sale.objects.create(value=total)
        cart.delete()
        return redirect('restaurant:cart_index')
