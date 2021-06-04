from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guildslist/', views.guildslist, name='guildslist'),
    path('oauth2/login', views.discordlogin, name='discordlogin'),
    path('oauth2/login/redirect', views.discordloginredirect, name='discordloginredirect'),
    path('changeprivileges/', views.changeprivileges, name='changeprivileges'),
]