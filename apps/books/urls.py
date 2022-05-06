from django.urls import path
from .views import books

urlpatterns = [
    path('', books.index, name='books_index'),
    path('create/', books.create, name='books_create'),
    path('update/<int:pk>/', books.update, name='books_update'),
    path('delete/<int:pk>/', books.delete, name='books_delete'),
]

