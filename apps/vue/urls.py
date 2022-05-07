from django.urls import path

from vue.views import books

app_name = 'vue'
urlpatterns = [
    path('', books.index, name='books_index'),
]
