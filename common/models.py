from django.db import models

from players.models import Player


# Create your models here.
class Award(models.Model):
    class AwardChoices(models.TextChoices):
        MVP = 'MVP', 'Most Valuable Player'
        MIP = 'MIP', 'Most Improved Player'
        DPOY = 'DPOY', 'Defensive Player of the Year'
        REB = 'REB', 'Rebounder of the Year'
        SCORING = 'SCORING', 'Scoring Title'
        ASSIST = 'ASSIST', 'Assist Champion'


    title = models.CharField(max_length=100, choices=AwardChoices.choices)
    year = models.PositiveIntegerField()
    players= models.ManyToManyField(Player)


    def __str__(self):
        return f"{self.title} ({self.year})"