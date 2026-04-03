from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('teams/', include('teams.urls')),
    path('games/', include('games.urls')),
    path('players/', include('players.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('BasketballLeague.api_urls')),
]

