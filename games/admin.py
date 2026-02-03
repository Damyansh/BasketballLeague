from django.contrib import admin

from games.models import Game


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'date', 'home_score', 'away_score')
    list_filter = ('home_team', 'away_team')
    search_fields = ('home_team__name', 'away_team__name')

