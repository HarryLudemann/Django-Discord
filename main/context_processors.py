from register.models import Themes
from main.models import Guilds

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

# Returns object of owned guilds
def GetGuilds(response):
    obj = Guilds.objects.all()
    for item in obj:
        print(item.name)
    obj = obj.filter(userid=response.user.id)
    return obj

def add_variable_to_context(request):
    Theme = CheckDarkTheme(request)
    Guilds = GetGuilds(request)
    return {
        'theme': Theme,
        'guilds': Guilds
    }
