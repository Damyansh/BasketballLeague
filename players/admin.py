from django.contrib import admin

from players.models import Player


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'team', 'points_per_game', 'rebounds_per_game', 'assists_per_game')
    list_filter = ('team', 'position', 'rebounds_per_game', 'assists_per_game', 'points_per_game')
    search_fields = ('first_name', 'last_name')