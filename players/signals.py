from django.db.models.signals import post_delete
from django.dispatch import receiver

from common.models import Award
from players.models import Player


@receiver(post_delete, sender=Player)
def delete_awards_without_players(sender, instance, **kwargs):
    awards = Award.objects.all()

    for award in awards:
        if not award.players.exists():
            award.delete()