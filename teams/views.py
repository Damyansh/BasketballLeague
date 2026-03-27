from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from common.permissions import IsAdminOrReadOnly
from teams.forms import TeamForm, TeamDeleteForm
from teams.models import Team
from teams.serializers import TeamSerializer


# Create your views here.


class TeamCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/team-add-page.html'
    success_url = reverse_lazy('common:home')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()



class TeamDetailView(DetailView):
    model = Team
    template_name = 'teams/team-details-page.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = self.object.players.all().order_by('first_name', 'last_name')
        return context



class TeamUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'teams/team-edit-page.html'
    context_object_name = 'team'

    def get_success_url(self):
        return reverse_lazy('teams:details', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()


class TeamDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Team
    template_name = 'teams/team-delete-page.html'
    context_object_name = 'team'
    success_url = reverse_lazy('common:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeamDeleteForm(instance=self.object)
        return context

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()


class TeamListView(ListView):
    model = Team
    template_name = 'teams/team-list-page.html'
    context_object_name = 'teams'
    paginate_by = 6

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        qs=Team.objects.all()
        if sort == 'name':
            qs=qs.order_by('name')
        elif sort == 'city':
            qs=qs.order_by('city')
        elif sort == 'year':
            qs=qs.order_by('-year_founded')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = context['page_obj']
        return context

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]