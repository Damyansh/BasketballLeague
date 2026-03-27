from rest_framework.routers import DefaultRouter

from games.views import GameViewSet
from players.views import PlayerViewSet
from teams.views import TeamViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = router.urls