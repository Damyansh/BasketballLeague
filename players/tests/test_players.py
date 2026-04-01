from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from players.models import Player
from teams.models import Team


class PlayerTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.player = Player.objects.create(
            first_name ="Test",
            last_name = "Player",
            position = "PG",
            points_per_game = 0,
            rebounds_per_game = 0,
            assists_per_game = 0,
            team = self.team,
            photo = "defaults/player.png"

        )


    def test_player_created(self):
        self.assertEqual(self.player.first_name, "Test")
        self.assertEqual(self.player.last_name, "Player")

    def test_player_str(self):
        self.assertEqual(str(self.player), f"{self.player.first_name} {self.player.last_name} ({self.player.team.name})")

    def test_player_list_view(self):
        response = self.client.get(reverse('players:list'))
        self.assertEqual(response.status_code, 200)

    def test_player_detail_view(self):
        response = self.client.get(reverse('players:details', args=[self.player.id]))
        self.assertEqual(response.status_code, 200)

    def test_player_create_requires_login(self):
        response = self.client.get(reverse('players:add'))
        self.assertEqual(response.status_code, 302)

    def test_logged_user_cannot_access_create(self):
        user=User.objects.create_user(username='test',password='pass')
        self.client.login(username='test', password='pass')
        response = self.client.get(reverse('players:add'))
        self.assertEqual(response.status_code, 403)

    def test_admin_can_access_create(self):
        user=User.objects.create_user(username='test',password='pass')
        admin_group = Group.objects.create(name='Admin')

        user.groups.add(admin_group)

        self.client.login(username='test', password='pass')
        response = self.client.get(reverse('players:add'))
        self.assertEqual(response.status_code, 200)