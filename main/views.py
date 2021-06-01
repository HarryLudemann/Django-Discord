
import functions
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from register.models import Themes
from main.models import Privileges
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
            guildid=form.cleaned_data["guildid"]
            #check if setting already excist and delete
            obj = Privileges.objects.all()
            if (obj.filter(userid=response.user.id).exists()):
                obj.filter(userid=response.user.id).delete()
            # save
            obj = Privileges(userid=response.user.id, identifier=form.cleaned_data["identifier"], funinspire=form.cleaned_data["funinspire"], funcomeback=form.cleaned_data["funcomeback"], funcat=form.cleaned_data["funcat"], fundog=form.cleaned_data["fundog"], funfox=form.cleaned_data["funfox"], basicping=form.cleaned_data["basicping"], adminquit=form.cleaned_data["adminquit"], adminchangeprefix=form.cleaned_data["adminchangeprefix"], admintest=form.cleaned_data["admintest"])
            obj.save()
            messages.success(response, 'Prefix Changed')
            print(functions.GetConfigValue('identifier', guildid))
            return redirect('/')
        else:  
            form = ChangePrivileges()
            return render(response, "main/changeprefix.html", {'form':form})
    else:
        form = ChangePrivileges()
    return render(response, "main/changeprefix.html", {'form':form})
