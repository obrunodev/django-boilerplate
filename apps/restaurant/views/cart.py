from django.shortcuts import redirect, render, get_object_or_404

from restaurant.models import Product
from restaurant.models import Cart


def cart_index(request):
    cart = Cart.objects.all()

    total = 0
    for item in cart:
        total += item.product.price

    context = {
        'products': Product.objects.all(),
        'cart': cart,
        'total': total
    }
    return render(request, 'cart/pages/index.html', context)


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # FIXME Somente a instância Product já é suficiente (Corrigir model)
    Cart.objects.create(
        product=product,
        cost=product.price,
    )
    product.quantity -= 1
    product.save()
    return redirect('restaurant:cart_index')


def remove_from_cart(request):
    pass
