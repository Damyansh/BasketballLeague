from django.db import models

from players.models import Player


# Create your models here.
class Award(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    players= models.ManyToManyField(Player)


    def __str__(self):
        return f"{self.title} ({self.year})"