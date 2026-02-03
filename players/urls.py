from django.urls import path, include

from players import views

app_name = 'players'

player_patterns = [
    path('',views.player_details, name = 'details'),
    path('edit/',views.player_edit, name = 'edit'),
    path('delete/',views.player_delete, name = 'delete'),
]
urlpatterns = [
    path('add/',views.player_add, name = 'add'),
    path('<int:pk>/',include(player_patterns))

]