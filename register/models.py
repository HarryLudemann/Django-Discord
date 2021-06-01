from django.db import models


class Themes(models.Model):
    theme = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)

    def __str__(self):
        return self.theme
        return self.userid