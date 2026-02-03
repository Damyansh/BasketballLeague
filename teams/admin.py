from django.contrib import admin

from teams.models import Team


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'year_founded', 'coach_name')
    list_filter = ('name', 'city', 'year_founded')
    search_fields = ('name', 'city', 'year_founded', 'coach_name')