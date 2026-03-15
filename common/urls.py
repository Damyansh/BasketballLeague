from django.urls import path

from common import views
from common.views import HomePageView, AwardCreateView, AwardUpdateView, AwardDeleteView

app_name = 'common'
urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('awards/add/',AwardCreateView.as_view(), name = 'award_add'),
    path('awards/<int:pk>/edit/<int:player_id>/',AwardUpdateView.as_view(), name = 'award_edit'),
    path('awards/<int:pk>/delete/<int:player_id>/',AwardDeleteView.as_view(), name = 'award_delete'),

]