from django.test import Client, TestCase
from django.urls import reverse

from .models import Player


class ProjectTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.player = Player.objects.create(name='qwerty')

    def test_player_str(self):
        self.assertEqual('qwerty', str(self.player))

    def test1(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test2(self):
        response = self.client.get(reverse('result', args=[self.player]))
        self.assertEqual(response.status_code, 200)

    def test_error(self):
        response = self.client.get('/eee')
        self.assertEqual(response.status_code, 404)
