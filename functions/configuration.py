from ..main.models import Privileges

# Create Config File
def CreateConfigFile(GuildID):
    obj = Privileges.objects.all()
    if (Privileges.objects(guildid=GuildID).exists()):
        obj.filter(guildid=GuildID).delete()
    obj = Privileges(guildid=GuildID, userid=None, identifier=None, funinspire=None, funcomeback=None, funcat=None, fundog=None, funfox=None, basicping=None, adminquit=None, adminchangeprefix=None, admintest=None)
    obj.save()

# Get Saved Config Value
def GetConfigValue(Value, GuildID):
    obj = Privileges.objects.all()
    if (obj.objects(guildid=GuildID).exists()):
        pass
    else:
        CreateConfigFile(GuildID)
    item = Privileges.objects.get(guildid=GuildID)
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
    obj = Privileges.objects.all()
    # check item excists in table
    if (obj.objects(guildid=GuildID).exists()):
        pass
    else:
        CreateConfigFile(GuildID)
    #set value
    item = Privileges.objects.get(guildid=GuildID)
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
    

if (__name__ == "__main__"):
    CreateConfigFile('677326100686438430') # GuildID For HAX00R
