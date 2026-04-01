from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from teams.models import Team


class TeamTests(TestCase):

    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            city='Test City',
            year_founded=2020,
            coach_name='Test Coach',
        )

    def test_team_created(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.city, 'Test City')
        self.assertEqual(self.team.year_founded, 2020)
        self.assertEqual(self.team.coach_name, 'Test Coach')

    def test_team_str(self):
        self.assertEqual(str(self.team), self.team.name)

    def test_team_list_view(self):
        response = self.client.get(reverse('teams:list'))
        self.assertEqual(response.status_code, 200)

    def test_team_detail_view(self):
        response = self.client.get(reverse('teams:details', args=[self.team.id]))
        self.assertEqual(response.status_code, 200)

    def test_team_create_requires_login(self):
        response = self.client.get(reverse('teams:add'))
        self.assertEqual(response.status_code, 302)

    def test_logged_user_cannot_create_team(self):
        user=User.objects.create_user(username='test',password='pass')
        self.client.login(username='test', password='pass')
        response = self.client.get(reverse('teams:add'))
        self.assertEqual(response.status_code, 403)

    def test_admin_can_create_team(self):
        user = User.objects.create_user(username='admin', password='pass')
        admin_group = Group.objects.create(name='Admin')

        user.groups.add(admin_group)

        self.client.login(username='admin', password='pass')
        response = self.client.get(reverse('teams:add'))
        self.assertEqual(response.status_code, 200)