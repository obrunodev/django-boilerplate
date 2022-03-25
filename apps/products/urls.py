from django.urls import path

from .views import products

app_name = 'products'
urlpatterns = [
    path('', products.products_index, name='index'),
    path('<int:product_id>/', products.product_detail, name='detail'),
    path('create/', products.products_create, name='create'),
    path('<int:product_id>/update/', products.products_update, name='update'),
    path('<int:product_id>/delete/', products.products_delete, name='delete'),
]
