from register.models import Themes
from main.models import Guilds, ConnectedGuilds

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


def add_variable_to_context(request):
    Theme = CheckDarkTheme(request)
    Guilds = GetGuilds(request)
    ConnectedGuildObjects = ConnectedGuilds.objects.all()
    ConnectedGuildIDs = []
    for item in ConnectedGuildObjects:
        ConnectedGuildIDs.append(item.guildid)
    
    return {
        'theme': Theme,
        'guilds': Guilds,
        'botsguilds': ConnectedGuildIDs,
        'discord_addbot': 'https://discord.com/api/oauth2/authorize?client_id='+ os.getenv("CLIENT_ID") +'&permissions=8&redirect_uri=https%3A%2F%2F' + os.getenv("DOMAIN") + '%2Foauth2%2Flogin%2Fredirect&scope=bot'
    }
