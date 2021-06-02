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

