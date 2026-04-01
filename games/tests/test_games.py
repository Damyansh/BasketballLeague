import datetime

from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse

from games.models import Game
from teams.models import Team


class GamesTest(TestCase):
    def setUp(self):
        self.team1 = Team.objects.create(name='Team 1', city='City 1')
        self.team2 = Team.objects.create(name='Team 2', city='City 2')

        self.game=Game.objects.create(
            date=datetime.date.today(),
            home_team=self.team1,
            away_team=self.team2,
            home_score=100,
            away_score=90,
        )

    def test_game_created(self):
        self.assertEqual(self.game.home_team, self.team1)
        self.assertEqual(self.game.away_team, self.team2)
        self.assertEqual(self.game.home_score, 100)
        self.assertEqual(self.game.away_score, 90)

    def test_game_str(self):
        self.assertIn(self.team1.name, str(self.game))
        self.assertIn(self.team2.name, str(self.game))

    def test_game_list_view(self):
        response = self.client.get(reverse('games:list'))
        self.assertEqual(response.status_code, 200)

    def test_game_detail_view(self):
        response = self.client.get(reverse('games:details', args=[self.game.id]))
        self.assertEqual(response.status_code, 200)

    def test_game_create_requires_login(self):
        response = self.client.get(reverse('games:add'))
        self.assertEqual(response.status_code, 302)

    def test_logged_user_cannot_create_game(self):
        user=User.objects.create_user(username='test',password='pass')
        self.client.login(username='test', password='pass')
        response = self.client.get(reverse('games:add'))
        self.assertEqual(response.status_code, 403)

    def test_admin_can_create_game(self):
        user = User.objects.create_user(username='admin', password='pass')
        admin_group = Group.objects.create(name='Admin')

        user.groups.add(admin_group)

        self.client.login(username='admin', password='pass')
        response = self.client.get(reverse('games:add'))
        self.assertEqual(response.status_code, 200)