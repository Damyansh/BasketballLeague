from django.db.models import Q

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from games.forms import GameForm, GameDeleteForm, GamePlayerStatsForm, GamePlayerStatsEditForm
from games.models import Game, GamePlayerStats
from teams.models import Team


# Create your views here.



class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game-add-page.html'
    success_url = reverse_lazy('common:home')



class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game-edit-page.html'
    context_object_name = 'game'

    def get_success_url(self):
        return reverse('games:details', kwargs={'pk': self.object.pk})


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game-details-page.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.object.player_stats.select_related('player', 'player__team')
        return context





class GameDeleteView(DeleteView):
    model = Game
    template_name = 'games/game-delete-page.html'
    context_object_name = 'game'
    success_url = reverse_lazy('common:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=GameDeleteForm(instance=self.object)
        return context




class GameAddStatsView(FormView):
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




class GameEditStatsView(UpdateView):
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






class GameDeleteStatsView(DeleteView):
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