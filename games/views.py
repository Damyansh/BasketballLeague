from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from games.forms import GameForm, GameDeleteForm, GamePlayerStatsForm
from games.models import Game, GamePlayerStats
from players.models import Player


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
        form = GamePlayerStatsForm(request.POST)
        if form.is_valid():
            stat = form.save(commit=False)
            stat.game = game
            stat.full_clean()
            stat.save()
            return redirect('games:details', pk=game.pk)

    else:
        form = GamePlayerStatsForm()

        form.fields['player'].queryset = Player.objects.filter(team__in=[game.home_team, game.away_team])

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'games/game-add-stats-page.html', context)


def game_edit_stats(request: HttpRequest, pk:int, stat_pk:int)-> HttpResponse:
    game = get_object_or_404(Game, pk=pk)
    stat=get_object_or_404(GamePlayerStats, pk=stat_pk, game=game)

    if request.method == "POST":
        form = GamePlayerStatsForm(request.POST, instance=stat)
        if form.is_valid():
            updated_stat = form.save(commit=False)
            updated_stat.game = game
            updated_stat.full_clean()
            updated_stat.save()
            return redirect('games:details', pk=game.pk)

    else:
        form = GamePlayerStatsForm(instance=stat)

        form.fields['player'].queryset = Player.objects.filter(team__in=[game.home_team, game.away_team])

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