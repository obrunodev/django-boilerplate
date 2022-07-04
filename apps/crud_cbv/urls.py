from django.urls import path

from .views import crud

app_name = 'crud_cbv'
urlpatterns = [
    path('', crud.index, name='index'),
]
