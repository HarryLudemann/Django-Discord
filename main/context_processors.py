from register.models import Themes
from main.models import Privileges

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

def GetGuilds(response):
    obj = Privileges.objects.all()
    if (obj.filter(guildowner=response.user.discord_tag).exists()):
        obj = obj.filter(guildid=response.user.discord_tag)
        return obj
    else:
        return None

def add_variable_to_context(request):
    Theme = CheckDarkTheme(request)
    Guilds = GetGuilds(request)
    return {
        'theme': Theme,
        'Guilds': Guilds
    }
