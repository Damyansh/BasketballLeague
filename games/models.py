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
    players = models.ManyToManyField(Player, through='GamePlayerStats', related_name='games')


    def clean(self):
        if self.home_team == self.away_team:
            raise ValidationError("A team cannot play against itself.")


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"

class GamePlayerStats(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='player_stats')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='game_stats')
    points = models.PositiveIntegerField(default=0)
    rebounds = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)


    def clean(self):
        if not self.game_id:
            return
        if self.player.team not in [self.game.home_team, self.game.away_team]:
            raise ValidationError("Player doesnt belong to either team in this game.")

    class Meta:
        unique_together = ('game', 'player')


    def __str__(self):
        return f"{self.player} - {self.game}"
