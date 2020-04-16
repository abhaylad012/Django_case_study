from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('header', views.header, name='header'),
    path('add_user', views.add_user, name='add_user'),
    path('login_verify', views.verify_user, name='login_verify'),
    path('logout', views.logout, name='logout'),

]