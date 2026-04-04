from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from rest_framework.viewsets import ModelViewSet

from common.permissions import IsAdminOrReadOnly
from games.forms import GameForm, GameDeleteForm, GamePlayerStatsForm, GamePlayerStatsEditForm
from games.models import Game, GamePlayerStats
from games.serializers import GameSerializer
from teams.models import Team
from games.tasks import notify_new_game


# Create your views here.



class GameCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game-add-page.html'
    success_url = reverse_lazy('common:home')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    def form_valid(self, form):
        response = super().form_valid(form)

        if settings.DEBUG:
            notify_new_game.delay(
                self.object.home_team.name,
                self.object.away_team.name
            )
        else:
            notify_new_game(
                self.object.home_team.name,
                self.object.away_team.name
            )

        return response

class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game-edit-page.html'
    context_object_name = 'game'

    def get_success_url(self):
        return reverse('games:details', kwargs={'pk': self.object.pk})
    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game-details-page.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.object.player_stats.select_related('player', 'player__team')
        return context





class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    template_name = 'games/game-delete-page.html'
    context_object_name = 'game'
    success_url = reverse_lazy('common:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=GameDeleteForm(instance=self.object)
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()


class GameAddStatsView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'games/game-add-stats-page.html'
    form_class = GamePlayerStatsForm

    def dispatch(self, request, *args, **kwargs):
        self.game = Game.objects.get(pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['game'] = self.game
        return kwargs

    def form_valid(self, form):
        stat = form.save(commit=False)
        stat.game = self.game
        stat.full_clean()
        stat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('games:details', kwargs={'pk': self.game.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.game
        return context


    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

class GameEditStatsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GamePlayerStats
    form_class = GamePlayerStatsEditForm
    template_name = 'games/game-edit-stats-page.html'
    context_object_name = 'stat'
    pk_url_kwarg = 'stat_pk'

    def get_success_url(self):
        return reverse('games:details', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(pk=self.kwargs['pk'])
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()






class GameDeleteStatsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GamePlayerStats
    template_name = 'games/game-delete-stats-page.html'
    pk_url_kwarg = 'stat_pk'
    context_object_name = 'stat'

    def get_success_url(self):
        return reverse('games:details', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(pk=self.kwargs['pk'])
        return context
    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()



class GameListView(ListView):
    model = Game
    template_name = 'games/game-list-page.html'
    context_object_name = 'games'
    paginate_by = 5

    def get_queryset(self):
        qs= Game.objects.all()
        team_id = self.request.GET.get('team')
        date = self.request.GET.get('date')

        if date:
            qs = qs.filter(date=date)

        if team_id:
            qs = qs.filter(Q(home_team_id=team_id) | Q(away_team_id=team_id))

        return qs.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['games'] = context['page_obj']

        return context


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminOrReadOnly]
