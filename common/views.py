from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from common.forms import AwardForm, AwardUpdateForm
from common.models import Award
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

def award_add(request: HttpRequest)-> HttpResponse:
    if request.method == "POST":
        form = AwardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('common:home')
    else:
        form = AwardForm()

    context = {
        'form': form
        }

    return render(request, 'common/award_add.html', context)


def award_edit(request: HttpRequest, pk:int, player_id)-> HttpResponse:
    award = get_object_or_404(Award, pk=pk)

    if request.method == "POST":
        form = AwardUpdateForm(request.POST, instance=award)
        if form.is_valid():
            form.save()
            return redirect('players:details', pk=player_id)
    else:
        form = AwardUpdateForm(instance=award)

    context = {
        'form': form
        }

    return render(request, 'common/award_edit.html', context)


def award_delete(request: HttpRequest, pk:int, player_id)-> HttpResponse:
    award = get_object_or_404(Award, pk=pk)

    if request.method == "POST":
        award.delete()
        return redirect('players:details', pk=player_id)

    context = {
        'award': award
        }

    return render(request, 'common/award_delete.html', context)