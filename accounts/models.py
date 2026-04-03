from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

from teams.models import Team


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    favourite_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True)

    profile_picture = CloudinaryField('image', null=True, blank=True)


    def __str__(self):
        return self.user.username