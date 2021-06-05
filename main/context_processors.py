from register.models import Themes
from main.models import Guilds
from bot import client

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

# Returns object of users owned guilds
def GetGuilds(response):
    obj = Guilds.objects.all()
    for item in obj:
        print(item.name)
    obj = obj.filter(userid=response.user.id)
    return obj

# Gets list of guilds connected to bot
def GetBotGuilds():
  Guilds = []
  for guild in client.guilds:              
    Guilds.append(guild.id)
  return Guilds

def add_variable_to_context(request):
    Theme = CheckDarkTheme(request)
    Guilds = GetGuilds(request)
    BotsGuilds = GetBotGuilds()
    return {
        'theme': Theme,
        'guilds': Guilds,
        'botsguilds': BotsGuilds
    }
