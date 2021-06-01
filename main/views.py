
import functions
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from register.models import Themes
from django.contrib.auth.decorators import login_required
from .forms import ChangePrivileges
import functions


def home(response):
    return render(response, "main/home.html", {})

@login_required
def changeprivileges(response):
    if response.method == "POST":
        form = ChangePrivileges(response.POST)
        if form.is_valid():
            guildid=form.cleaned_data["GuildID"]
            newprefix=form.cleaned_data["Prefix"]
            functions.SetConfigValue('identifier', newprefix, guildid)
            messages.success(response, 'Prefix Changed')
            print(functions.GetConfigValue('identifier', guildid))
            return redirect('/')
        else:  
            form = ChangePrivileges()
            return render(response, "main/changeprefix.html", {'form':form})
    else:
        form = ChangePrivileges()
    return render(response, "main/changeprefix.html", {'form':form})
