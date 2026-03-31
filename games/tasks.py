from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def notify_new_game(home_team, away_team):
    logger.info(f"[CELERY] New game created: {home_team} vs {away_team}")