from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import RegisterForm, ProfileForm
from accounts.models import Profile


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)

        fan_group=Group.objects.get(name='Fan')
        self.object.groups.add(fan_group)

        return response

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('common:home')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile-edit.html'

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return reverse('accounts:profile')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('common:home')

    def get_object(self):
        return self.request.user


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change-password.html'

    def get_success_url(self):
        return reverse('common:home')