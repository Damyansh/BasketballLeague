from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def notify_new_player(player_name):
    logger.info(f"[CELERY] New player created: {player_name}")