from django.urls import path, include

from teams import views
from teams.views import TeamListView, TeamCreateView, TeamDetailView, TeamUpdateView, TeamDeleteView

app_name = 'teams'

team_patterns = [
    path('',TeamDetailView.as_view(), name = 'details'),
    path('edit/',TeamUpdateView.as_view(), name = 'edit'),
    path('delete/',TeamDeleteView.as_view(), name = 'delete'),
]

urlpatterns = [
    path('',TeamListView.as_view(), name = 'list'),
    path('add/',TeamCreateView.as_view(), name = 'add'),
    path('<int:pk>/',include(team_patterns))

]