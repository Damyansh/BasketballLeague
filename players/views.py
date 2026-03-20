from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from common.models import Award
from players.forms import PlayerForm, PlayerDeleteForm
from players.models import Player
from teams.models import Team


# Create your views here.


class PlayerCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player-add-page.html'
    success_url = reverse_lazy('common:home')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()


class PlayerUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player-edit-page.html'
    context_object_name = 'player'

    def get_success_url(self):
        return reverse_lazy('players:details', kwargs={'pk': self.object.pk})


    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()
class PlayerDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Player
    template_name = 'players/player-delete-page.html'
    context_object_name = 'player'
    success_url = reverse_lazy('common:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlayerDeleteForm(instance=self.object)
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()
class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player-details-page.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['awards'] = Award.objects.filter(players=self.object)
        return context




class PlayerListView(ListView):
    model = Player
    template_name = 'players/player-list-page.html'
    context_object_name = 'players'
    paginate_by = 8

    def get_queryset(self):
        team_id = self.request.GET.get('team')
        sort = self.request.GET.get('sort')

        qs = Player.objects.all()

        if team_id:
            qs = qs.filter(team_id=team_id)

        if sort == 'name':
            qs = qs.order_by('first_name', 'last_name')
        elif sort == 'team':
            qs = qs.order_by('team__name')
        elif sort == 'points':
            qs = qs.order_by('-points_per_game')
        elif sort == 'rebounds':
            qs = qs.order_by('-rebounds_per_game')
        elif sort == 'assists':
            qs = qs.order_by('-assists_per_game')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['players'] =context['page_obj']
        return context