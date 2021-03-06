from django.db import models
from .managers import DiscordUserOAuth2Manager

class Privileges(models.Model):
    userid = models.CharField(max_length=50)
    guildid = models.CharField(max_length=50)
    identifier = models.CharField(max_length=50)
    funinspire = models.CharField(max_length=50)
    funcomeback = models.CharField( max_length=50)
    funcat = models.CharField(max_length=50)
    fundog = models.CharField(max_length=50)
    funfox = models.CharField(max_length=50)
    basicping = models.CharField( max_length=50)
    adminquit = models.CharField(max_length=50)
    adminchangeprefix = models.CharField(max_length=50)
    admintest = models.CharField(max_length=50)

class DiscordUser(models.Model):
    objects = DiscordUserOAuth2Manager()
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    discord_tag = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self, request):
        return True

# User Guilds
class Guilds(models.Model):
    userid = models.CharField(max_length=50)
    guildid = models.BigIntegerField()
    name = models.CharField(max_length=150)
    icon = models.CharField(max_length=100)

# Guilds Connected to bots
class ConnectedGuilds(models.Model):
    guildid = models.BigIntegerField()