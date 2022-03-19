
import functions
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from register.models import Themes
from main.models import Privileges, Guilds
from django.contrib.auth.decorators import login_required
from .forms import ChangePrivileges
import functions
import requests
import os
from django.contrib.auth import authenticate, login

discord_login = 'https://discord.com/api/oauth2/authorize?client_id='+ os.getenv("CLIENT_ID") +'&redirect_uri=https%3A%2F%2F' + os.getenv("DOMAIN") + '%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify%20email%20guilds'

def exchange_code(code):
    """ Exchange the code for a token. """
    data = {
        'client_id' : os.getenv("CLIENT_ID"),
        'client_secret' : os.getenv("CLIENT_SECRET"),
        'grant_type' : 'authorization_code',
        'code' : code,
        'redirect_uri' : 'https://' + os.getenv("DOMAIN") + '/oauth2/login/redirect',
        'scope': 'identify email guilds'
    }
    headers = {
        'Content_Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get("https://discord.com/api/v6/users/@me", headers={'Authorization':'Bearer %s' %access_token})
    response2 = requests.get("https://discord.com/api/v6/users/@me/guilds", headers={'Authorization':'Bearer %s' %access_token})
    guildslist = response2.json()
    user = response.json()
    
    #check if guilds already excist for user and delete
    obj = Guilds.objects.all()
    # if (obj.filter(userid=user['id']).exists()):
    #     obj.filter(userid=user['id']).delete()
    
    # remove all guilds with the users id
    for item in obj:
        if (item.userid == user['id']):
            item.delete()

    for n in range(len(guildslist)):
        if (str(guildslist[n]['owner']) == 'True'):
            obj = Guilds(userid=user['id'], guildid=guildslist[n]['id'], name=guildslist[n]['name']) # icon=guildslist[n]['icon'],
            obj.save()
    return user

def home(response):
    return render(response, "main/home.html", {})

def discordlogin(response):
    return redirect(discord_login)

def discordloginredirect(response):
    login(response, authenticate(response, user=exchange_code(response.GET.get('code'))))
    # update servers available
    return redirect("/dashboard")

@login_required(login_url='/oauth2/login')
def changeprivileges(response, id):
    ownedguildids = []
    obj = Guilds.objects.filter(userid=response.user.id)
    for item in obj:
        ownedguildids.append(item.guildid)
    if (id in ownedguildids):
        obj = Privileges.objects.all()
        if response.method == "POST":
            form = ChangePrivileges(response.POST)
            if form.is_valid():
                #check if setting already excist and delete
                if (obj.filter(guildid=id).exists()):
                    obj.filter(guildid=id).delete()
                # save
                obj = Privileges(guildid=id, userid=response.user.id, identifier=form.cleaned_data["identifier"], funinspire=form.cleaned_data["funinspire"], funcomeback=form.cleaned_data["funcomeback"], funcat=form.cleaned_data["funcat"], fundog=form.cleaned_data["fundog"], funfox=form.cleaned_data["funfox"], basicping=form.cleaned_data["basicping"], adminquit=form.cleaned_data["adminquit"], adminchangeprefix=form.cleaned_data["adminchangeprefix"], admintest=form.cleaned_data["admintest"])
                obj.save()
                messages.success(response, 'Prefix Changed')
                return redirect('/dashboard')
            else:  
                functions.CreateConfigFile(id)
                redirect('/')
        else:
            if (obj.filter(guildid=id).exists()):
                obj = obj.filter(guildid=id)
                for item in obj: #filter only iterable only run once
                    form = ChangePrivileges(initial={'guildid':item.guildid,'identifier':item.identifier, 'funinspire':item.funinspire, 'funcomeback':item.funcomeback, 'funcat':item.funcat, 'fundog':item.fundog, 'funfox':item.funfox, 'basicping':item.basicping, 'adminquit':item.adminquit, 'adminchangeprefix':item.adminchangeprefix,'admintest':item.admintest})
            else:
                form = ChangePrivileges()
        return render(response, "main/changeprivileges.html", {'form':form})
    else:
        return redirect('/')

@login_required(login_url='/oauth2/login')
def dashboard(response):
    return render(response, "main/dashboard.html", {})

