from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from common.forms import AwardForm, AwardUpdateForm
from common.models import Award
from games.models import Game
from teams.models import Team


# Create your views here.



class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        teams_list = Team.objects.all()
        games_list= Game.objects.all().order_by('-date')

        team_paginator = Paginator(teams_list, 6)
        team_page_number = self.request.GET.get('team_page')
        teams = team_paginator.get_page(team_page_number)

        games_paginator = Paginator(games_list, 5)
        games_page_number = self.request.GET.get('game_page')
        games = games_paginator.get_page(games_page_number)

        context['teams'] = teams
        context['games'] = games

        return context


class AwardCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'common/award_add.html'
    success_url = reverse_lazy('common:home')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()




class AwardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Award
    form_class = AwardUpdateForm
    template_name = 'common/award_edit.html'

    def get_success_url(self):
        player_id = self.kwargs.get('player_id')
        return reverse('players:details', kwargs={'pk': player_id})

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()


class AwardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Award
    template_name = 'common/award_delete.html'

    def get_success_url(self):
        player_id = self.kwargs.get('player_id')
        return reverse('players:details', kwargs={'pk': player_id})

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()