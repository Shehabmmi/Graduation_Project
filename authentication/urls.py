from django.urls import path
from . import views

# www.mywebsite.com/register GET - return the template of the register
# www.mywebsite.com/register POST - getting data and the making the registration of the user

urlpatterns = [
    path('login', views.login),
    path('users', views.users),
    path('users/<int:id>', views.single_user),
]