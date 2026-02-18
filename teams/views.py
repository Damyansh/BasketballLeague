from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from teams.forms import TeamForm, TeamDeleteForm
from teams.models import Team


# Create your views here.

def team_add(request: HttpRequest)-> HttpResponse:
    form = TeamForm(request.POST or None , request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('common:home')

    context = {
        'form': form,
    }
    return render(request, 'teams/team-add-page.html', context)

def team_details(request: HttpRequest, pk:int)-> HttpResponse:
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all().order_by('first_name', 'last_name')
    context = {
        'team': team,
        'players': players,
    }
    return render(request, 'teams/team-details-page.html', context)

def team_edit(request: HttpRequest, pk:int)-> HttpResponse:
    team = get_object_or_404(Team, pk=pk)
    form = TeamForm(request.POST or None, request.FILES or None, instance=team)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('teams:details', pk=team.pk)

    context = {
        'form': form,
        'team': team,
    }
    return render(request, 'teams/team-edit-page.html', context)

def team_delete(request: HttpRequest, pk:int)-> HttpResponse:
    team = get_object_or_404(Team, pk=pk)
    form = TeamDeleteForm(request.POST or None, instance=team)
    if request.method == "POST":
        team.delete()
        return redirect('common:home')
    context = {
        'form': form,
        'team': team,
    }
    return render(request, 'teams/team-delete-page.html', context)

def team_list(request: HttpRequest)-> HttpResponse:
    sort = request.GET.get('sort')

    teams = Team.objects.all()

    if sort == 'name':
        teams= teams.order_by('name')
    elif sort == 'city':
        teams= teams.order_by('city')
    elif sort == 'year':
        teams= teams.order_by('-year_founded')

    context = {
        'teams': teams,
    }

    return render(request, 'teams/team-list-page.html', context)