from django.urls import path
from .views import books

urlpatterns = [
    path('', books.index, name='books_index'),
    path('create/', books.create, name='books_create'),
    path('update/<int:pk>/', books.update, name='books_update'),
    path('delete/<int:pk>/', books.delete, name='books_delete'),
    
    # Vue views
    path('vue/', books.index_view, name='index_view'),
    
    # API
    path('api/', books.index_json, name='books_index_json'),
]

