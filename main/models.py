from django.db import models

class Privileges(models.Model):
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