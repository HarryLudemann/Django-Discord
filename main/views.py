
import functions
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from register.models import Themes
from main.models import Privileges
from django.contrib.auth.decorators import login_required
from .forms import ChangePrivileges
import functions

discord_login = 'https://discord.com/api/oauth2/authorize?client_id=833177090350252072&redirect_uri=https%3A%2F%2Fhazzahsbot.herokuapp.com%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify'

def home(response):
    return render(response, "main/home.html", {})

def discordlogin(response):
    return redirect(discord_login)

def discordloginredirect(response):
    return redirect("/")

@login_required
def changeprivileges(response):
    obj = Privileges.objects.all()
    if response.method == "POST":
        form = ChangePrivileges(response.POST)
        if form.is_valid():
            #check if setting already excist and delete
            if (obj.filter(userid=response.user.id).exists()):
                obj.filter(userid=response.user.id).delete()
            # save
            obj = Privileges(guildid=form.cleaned_data["guildid"], userid=response.user.id, identifier=form.cleaned_data["identifier"], funinspire=form.cleaned_data["funinspire"], funcomeback=form.cleaned_data["funcomeback"], funcat=form.cleaned_data["funcat"], fundog=form.cleaned_data["fundog"], funfox=form.cleaned_data["funfox"], basicping=form.cleaned_data["basicping"], adminquit=form.cleaned_data["adminquit"], adminchangeprefix=form.cleaned_data["adminchangeprefix"], admintest=form.cleaned_data["admintest"])
            obj.save()
            messages.success(response, 'Prefix Changed')
            return redirect('/')
        else:  
            form = ChangePrivileges()
            return render(response, "main/changeprefix.html", {'form':form})
    else:
        if (obj.filter(userid=response.user.id).exists()):
            obj = obj.filter(userid=response.user.id)
            for item in obj: #filter only iterable only run once
                form = ChangePrivileges(initial={'guildid':item.guildid,'identifier':item.identifier, 'funinspire':item.funinspire, 'funcomeback':item.funcomeback, 'funcat':item.funcat, 'fundog':item.fundog, 'funfox':item.funfox, 'basicping':item.basicping, 'adminquit':item.adminquit, 'adminchangeprefix':item.adminchangeprefix,'admintest':item.admintest})
        else:
            form = ChangePrivileges()
    return render(response, "main/changeprefix.html", {'form':form})
