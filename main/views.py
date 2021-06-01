
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from register.models import Themes
from django.contrib.auth.decorators import login_required

# Checks theme
def CheckDarkTheme(response):
    obj = Themes.objects.all()
    if (obj.filter(userid=response.user.id).exists()):
        obj = obj.filter(userid=response.user.id)
        for item in obj:
            if (item.theme == "dark"):
                return 'dark'
            else:
                return 'light'
    else:
        return 'light'


def home(response):
    return render(response, "main/home.html", {"theme":CheckDarkTheme(response)})
