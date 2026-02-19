from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from games.forms import GameForm, GameDeleteForm, GamePlayerStatsForm, GamePlayerStatsEditForm
from games.models import Game, GamePlayerStats
from players.models import Player
from teams.models import Team


# Create your views here.


def game_add(request: HttpRequest)-> HttpResponse:
    form = GameForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('common:home')
    context = {
        'form': form,
    }
    return render(request, 'games/game-add-page.html', context)

def game_edit(request: HttpRequest, pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    form = GameForm(request.POST or None, instance=game)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('games:details', pk=game.pk)
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'games/game-edit-page.html', context)

def game_details(request: HttpRequest, pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    stats = game.player_stats.select_related('player', 'player__team')
    context = {
        'game': game,
        'stats': stats,
    }
    return render(request, 'games/game-details-page.html', context)


def game_delete(request: HttpRequest, pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    form=GameDeleteForm(request.POST or None, instance=game)

    if request.method == "POST":
        game.delete()
        return redirect('common:home')
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'games/game-delete-page.html', context)


def game_add_stats(request: HttpRequest, pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        form = GamePlayerStatsForm(request.POST,game=game)
        if form.is_valid():
            stat = form.save(commit=False)
            stat.game = game
            stat.full_clean()
            stat.save()
            return redirect('games:details', pk=game.pk)

    else:
        form = GamePlayerStatsForm(game=game)



    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'games/game-add-stats-page.html', context)


def game_edit_stats(request: HttpRequest, pk:int, stat_pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    stat=get_object_or_404(GamePlayerStats, pk=stat_pk, game=game)

    if request.method == "POST":
        form =GamePlayerStatsEditForm(request.POST, instance=stat)
        if form.is_valid():
            form.save()

            return redirect('games:details', pk=game.pk)

    else:
        form = GamePlayerStatsEditForm(instance=stat)



    context = {
        'form': form,
        'game': game,
        'stat': stat,
    }
    return render(request, 'games/game-edit-stats-page.html', context)


def game_delete_stats(request: HttpRequest, pk:int, stat_pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    stat=get_object_or_404(GamePlayerStats, pk=stat_pk, game=game)

    if request.method == "POST":
        stat.delete()
        return redirect('games:details', pk=game.pk)

    context = {
        'game': game,
        'stat': stat,
    }
    return render(request, 'games/game-delete-stats-page.html', context)

def game_list(request: HttpRequest)-> HttpResponse:
    team_id = request.GET.get('team')
    games = Game.objects.all()
    date = request.GET.get('date')

    if date:
        games = games.filter(date=date)

    if team_id:
        games=games.filter(Q(home_team_id=team_id) | Q(away_team_id=team_id))

    teams = Team.objects.all()

    games=games.order_by('-date')

    context = {
        'games': games,
        'teams': teams,
    }

    return render(request, 'games/game-list-page.html', context)