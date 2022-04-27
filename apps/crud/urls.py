from django.urls import path

from .views import books

app_name = 'crud'
urlpatterns = [
    path('', books.index, name='books_index'),
    path('<int:pk>', books.detail, name='books_detail'),
    path('new/', books.new, name='books_new'),
    path('create/', books.create, name='books_create'),
    path('<int:pk>/update/', books.update, name='books_update'),
    path('<int:pk>/delete/', books.delete, name='books_delete'),
]
