from django.urls import path, include
from games import views
app_name = 'games'
urlpatterns = [
    path('add/',views.game_add, name ='add'),
    path('<int:pk>/',include([
        path('', views.game_details, name='details'),
        path('edit/', views.game_edit, name='edit'),
        path('delete/', views.game_delete, name='delete'),
        path('add-stats/', views.game_add_stats, name='add-stats'),
        path('stats/<int:stat_pk>/edit/', views.game_edit_stats, name='edit-stats'),
        path('stats/<int:stat_pk>/delete/', views.game_delete_stats, name='delete-stats'),

    ]))

]