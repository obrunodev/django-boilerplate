from django.urls import path

from .views import categories
from .views import products
from .views import purchases
from .views import sales
from .views import cart

app_name = 'restaurant'
urlpatterns = [
    path('products/', products.products_index, name='products_index'),
    path('products/create/', products.products_create, name='products_create'),
    path('products/<int:product_id>/', products.product_detail, name='products_detail'),
    path('products/<int:product_id>/update/', products.products_update, name='products_update'),
    path('products/<int:product_id>/delete/', products.products_delete, name='products_delete'),

    path('categories/', categories.categories_index, name='categories_index'),
    path('categories/create/', categories.categories_create, name='categories_create'),
    path('categories/<int:category_id>/delete', categories.categories_delete, name='categories_delete'),

    path('purchases', purchases.purchase_index, name='purchases_index'),
    path('purchases/create/', purchases.purchase_create, name='purchases_create'),

    path('sales/', sales.sales_index, name='sales_index'),
    path('sales/finish/', sales.finish_order, name='finish_order'),

    path('cart/', cart.cart_index, name='cart_index'),
    path('cart/add/<int:pk>/', cart.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', cart.remove_from_cart, name='remove_from_cart'),
]
