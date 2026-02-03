from django.urls import path, include

from teams import views

app_name = 'teams'

team_patterns = [
    path('',views.team_details, name = 'details'),
    path('edit/',views.team_edit, name = 'edit'),
    path('delete/',views.team_delete, name = 'delete'),
]

urlpatterns = [
    path('add/',views.team_add, name = 'add'),
    path('<int:pk>/',include(team_patterns))

]