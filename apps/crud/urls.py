from django.urls import path

from .views import books

app_name = 'crud'
urlpatterns = [
    path('', books.index, name='books_index')
]
