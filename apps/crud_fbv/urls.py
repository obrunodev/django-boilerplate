from django.urls import path

from .views import crud

app_name = 'crud_fbv'
urlpatterns = [
    path('', crud.index, name='index'),
    path('create/', crud.create, name='create'),
    path('<int:pk>/update/', crud.update, name='update'),
    path('<int:pk>/delete/', crud.delete, name='delete'),
]
