from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import datetime

from teams.validators import LogoValidator


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    year_founded = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.date.today().year)],null=True, blank=True)
    logo = CloudinaryField('image', blank=True, null=True)
    coach_name = models.CharField(max_length=100,blank=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name