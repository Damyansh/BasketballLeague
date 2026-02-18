from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from common.models import Award
from players.forms import PlayerForm, PlayerDeleteForm
from players.models import Player
from teams.models import Team


# Create your views here.
def player_add(request: HttpRequest)-> HttpResponse:
    form = PlayerForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('common:home')

    context = {
        'form': form,
    }
    return render(request, 'players/player-add-page.html', context)

def player_edit(request: HttpRequest, pk:int)-> HttpResponse:
    player = get_object_or_404(Player, pk=pk)
    form = PlayerForm(request.POST or None, request.FILES or None, instance=player)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('players:details', pk=player.pk)
    context = {
        'form': form,
        'player': player,
    }
    return render(request, 'players/player-edit-page.html', context)

def player_delete(request: HttpRequest, pk:int)-> HttpResponse:
    player = get_object_or_404(Player, pk=pk)
    form= PlayerDeleteForm(request.POST or None, instance=player)
    if request.method == "POST":
        player.delete()
        return redirect('common:home')
    context = {
        'form': form,
        'player': player,
    }

    return render(request, 'players/player-delete-page.html', context)

def player_details(request: HttpRequest, pk:int)-> HttpResponse:
    player = get_object_or_404(Player, pk=pk)
    awards = Award.objects.filter(players=player)
    context = {
        'player': player,
        'awards': awards
    }

    return render(request, 'players/player-details-page.html', context)


def player_list(request: HttpRequest)-> HttpResponse:
    team_id = request.GET.get('team')
    sort = request.GET.get('sort')

    players = Player.objects.all()

    if team_id:
        players = players.filter(team_id=team_id)

    if sort == 'name':
        players= players.order_by('first_name', 'last_name')
    elif sort == 'team':
        players = players.order_by('team__name')
    elif sort == 'points':
        players = players.order_by('-points_per_game')
    elif sort == 'rebounds':
        players = players.order_by('-rebounds_per_game')
    elif sort == 'assists':
        players = players.order_by('-assists_per_game')

    paginator = Paginator(players, 8)
    page_number = request.GET.get('page')
    players = paginator.get_page(page_number)


    teams = Team.objects.all()

    context = {
        'players': players,
        'teams': teams,
    }

    return render(request, 'players/player-list-page.html', context)