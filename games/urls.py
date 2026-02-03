from django.urls import path, include
from games import views
app_name = 'games'
urlpatterns = [
    path('add/',views.game_add, name ='add'),
    path('<int:pk>/',include([
        path('', views.game_details, name='details'),
        path('edit/', views.game_edit, name='edit'),

    ]))

]