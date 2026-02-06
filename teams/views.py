from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from teams.models import Team


# Create your views here.

def team_add(request: HttpRequest)-> HttpResponse:
    return render(request, 'teams/team-add-page.html')

def team_details(request: HttpRequest, pk:int)-> HttpResponse:
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all()
    context = {
        'team': team,
        'players': players,
    }
    return render(request, 'teams/team-details-page.html', context)

def team_edit(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'teams/team-edit-page.html')

def team_delete(request: HttpRequest, pk:int)-> HttpResponse:
    return render(request, 'teams/team-delete-page.html')