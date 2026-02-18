from django import template


register = template.Library()

@register.filter
def player_count(team):
    return team.players.count()