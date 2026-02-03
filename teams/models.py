
from django.db import models

from teams.validators import LogoValidator


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    year_founded = models.PositiveIntegerField(null=True, blank=True)
    logo = models.ImageField(validators=[LogoValidator(2)], null=True, blank=True)
    coach_name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name