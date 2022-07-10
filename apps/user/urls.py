from django.urls import path

from .views import users

app_name = 'user'
urlpatterns = [
    path('signin/', users.signin, name='signin'),
    path('signup/', users.signup, name='signup'),
    path('logout/', users.logout, name='logout'),
    path('profile/', users.profile, name='profile'),
]
