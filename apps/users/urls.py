from django.urls import path

from .views import auth

app_name = 'users'
urlpatterns = [
    path('register/', auth.register, name='register'),
    path('login/', auth.login, name='login'),
    path('profile/', auth.profile, name='profile'),
]
