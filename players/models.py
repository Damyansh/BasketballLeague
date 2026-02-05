from django.db import models

# Create your models here.
class Player(models.Model):
    class PositionChoices(models.TextChoices):
        PG = 'PG', 'Point Guard'
        SG = 'SG', 'Shooting Guard'
        SF = 'SF', 'Small Forward'
        PF = 'PF', 'Power Forward'
        C = 'C', 'Center'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=2, choices=PositionChoices.choices)
    team = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='players')
    points_per_game = models.FloatField()
    rebounds_per_game = models.FloatField()
    assists_per_game = models.FloatField()
    photo =models.ImageField(upload_to='players/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"