from django.urls import path

from common import views

app_name = 'common'
urlpatterns = [
    path('',views.home_page, name = 'home'),
    path('awards/add/',views.award_add, name = 'award_add'),
    path('awards/<int:pk>/edit/<int:player_id>/',views.award_edit, name = 'award_edit'),
    path('awards/<int:pk>/delete/<int:player_id>/',views.award_delete, name = 'award_delete'),

]