# import database
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite.settings'
django.setup()
from main.models import Privileges, ConnectedGuilds

# Create Config File
def CreateConfigFile(GuildID):
    if (Privileges.objects.filter(guildid=GuildID).exists()):
        Privileges.objects.filter(guildid=GuildID).delete()
    obj = Privileges(guildid=GuildID, userid=" ", identifier=" ", funinspire=" ", funcomeback=" ", funcat=" ", fundog=" ", funfox=" ", basicping=" ", adminquit=" ", adminchangeprefix=" ", admintest=" ")
    obj.save()

# Get Saved Config Value
def GetConfigValue(Value, GuildID):
    obj = Privileges.objects.filter(guildid=GuildID)
    for item in obj:
        if Value == 'identifier': return item.identifier
        elif Value == 'fun-inspire': return item.funinspire
        elif Value == 'fun-comeback': return item.funcomeback
        elif Value == 'fun-cat': return item.funcat
        elif Value == 'fun-dog': return item.fundog
        elif Value == 'fun-fox': return item.funfox
        elif Value == 'basic-ping': return item.basicping
        elif Value == 'admin-quit': return item.adminquit
        elif Value == 'adminchangeprefix': return item.adminchangeprefix
        elif Value == 'admin-test': return item.admintest

# Set Config Value to file
def SetConfigValue(Value, NewValue, GuildID):
    obj = Privileges.objects.filter(guildid=GuildID)
    for item in obj:
        if Value == 'identifier': item.identifier = NewValue
        elif Value == 'fun-inspire': item.funinspire = NewValue
        elif Value == 'fun-comeback': item.funcomeback = NewValue
        elif Value == 'fun-cat': item.funcat = NewValue
        elif Value == 'fun-dog': item.fundog = NewValue
        elif Value == 'fun-fox': item.funfox = NewValue
        elif Value == 'basic-ping': item.basicping = NewValue
        elif Value == 'admin-quit': item.adminquit = NewValue
        elif Value == 'adminchangeprefix': item.adminchangeprefix = NewValue
        elif Value == 'admin-test': item.admintest = NewValue
        item.save()
    
# Update Connected Guilds
def UpdateConnectedGuilds(GuildsList):
    ConnectedGuilds.objects.all().delete()
    for item in GuildsList:
        obj = ConnectedGuilds(guildid=item)
        obj.save()
    obj = ConnectedGuilds.objects.all()
    print(str(obj.count()))
    

if (__name__ == "__main__"):
    CreateConfigFile('677326100686438430') # GuildID For HAX00R
