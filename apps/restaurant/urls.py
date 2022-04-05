from django.urls import path

from .views import categories
from .views import products

app_name = 'restaurant'
urlpatterns = [
    path('', products.products_index, name='products_index'),
    path('create/', products.products_create, name='products_create'),
    path('<int:product_id>/', products.product_detail, name='products_detail'),
    path('<int:product_id>/update/', products.products_update, name='products_update'),
    path('<int:product_id>/delete/', products.products_delete, name='products_delete'),

    path('categories/', categories.categories_index, name='categories_index'),
    path('categories/create/', categories.categories_create, name='categories_create'),
    path('categories/<int:category_id>/delete', categories.categories_delete, name='categories_delete'),
]
