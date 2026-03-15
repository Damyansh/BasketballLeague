from django.urls import path, include

from players import views
from players.views import PlayerListView, PlayerCreateView, PlayerDetailView, PlayerUpdateView, PlayerDeleteView

app_name = 'players'

player_patterns = [
    path('',PlayerDetailView.as_view(), name = 'details'),
    path('edit/',PlayerUpdateView.as_view(), name = 'edit'),
    path('delete/',PlayerDeleteView.as_view(), name = 'delete'),
]
urlpatterns = [
    path('',PlayerListView.as_view(), name = 'list'),
    path('add/',PlayerCreateView.as_view(), name = 'add'),
    path('<int:pk>/',include(player_patterns))

]