from django.urls import path, include
from games import views
from games.views import GameListView, GameCreateView, GameDetailView, GameUpdateView, GameDeleteView, GameAddStatsView, \
    GameEditStatsView, GameDeleteStatsView

app_name = 'games'
urlpatterns = [
    path('',GameListView.as_view(), name = 'list'),
    path('add/',GameCreateView.as_view(), name ='add'),
    path('<int:pk>/',include([
        path('', GameDetailView.as_view(), name='details'),
        path('edit/', GameUpdateView.as_view(), name='edit'),
        path('delete/', GameDeleteView.as_view(), name='delete'),
        path('add-stats/', GameAddStatsView.as_view(), name='add-stats'),
        path('stats/<int:stat_pk>/edit/', GameEditStatsView.as_view(), name='edit-stats'),
        path('stats/<int:stat_pk>/delete/', GameDeleteStatsView.as_view(), name='delete-stats'),

    ]))

]