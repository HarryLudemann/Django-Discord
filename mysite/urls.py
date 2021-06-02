"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from register import views as v
from django.contrib.auth import views as auth_views #import this

urlpatterns = [
    path('', include('main.urls')),
    path('register/', v.register, name="register"),
    path('editprofile/', v.editprofile, name="editprofile"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name="register/change-password.html")),
    # path('password/done',v.passworddone, name="passworddone"),
    path('admin/', admin.site.urls),
    # path('', include("django.contrib.auth.urls")),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path("password_reset/", v.password_reset_request, name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="register/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name='password_reset_complete'), 
    # path('', include("django.contrib.auth.urls")),
]