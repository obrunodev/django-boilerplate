from django.urls import path

from . import views

app_name = 'crud_fbv'
urlpatterns = [
    path('', views.index, name='index'),
]
