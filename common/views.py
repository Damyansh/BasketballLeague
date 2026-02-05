from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from games.models import Game
from teams.models import Team


# Create your views here.

def home_page(request: HttpRequest)-> HttpResponse:
    teams = Team.objects.all()
    games= Game.objects.all()

    context = {
        'teams': teams,
        'games': games
    }
    return render(request, 'common/home-page.html', context)