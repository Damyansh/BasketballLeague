from django.core.exceptions import ValidationError
from django.db import models

from players.models import Player


# Create your models here.
class Game(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='away_games')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    players = models.ManyToManyField(Player)

    def clean(self):
        if self.home_team == self.away_team:
            raise ValidationError("A team cannot play against itself.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"