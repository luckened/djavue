from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json

PENSOLOGO = 'Penso, logo existo!'
PRIMEIRALEI = 'A tendência dos corpos, quando nenhuma força é exercida sobre eles, ' \
              'é permanecer em seu estado natural, ou seja, repouso ou movimento retilíneo e uniforme.'
GRAVITACAO = 'Dois corpos no espaço se atram com uma força inversamente proporcional ' \
             'ao quadrado da distância entre eles.'
INSANIDADE = 'Insanidade é continuar fazendo sempre a mesma coisa e esperar resultados diferentes'


class TestTweetsApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.usuarios_cientistas()

    def test_tweets_api(self):
        newton, einstein, descartes, anon = Client(), Client(), Client(), Client()
        newton.force_login(User.objects.get(username='newton'))
        einstein.force_login(User.objects.get(username='einstein'))
        descartes.force_login(User.objects.get(username='descartes'))
        self._toggle_follow(newton, 'descartes', True)
        self._toggle_follow(einstein, 'descartes', True)
        self._toggle_follow(einstein, 'newton', True)
        self._toggle_follow(newton, 'einstein', True)
        self._toggle_follow(newton, 'einstein', False)
        self._tweet(descartes, PENSOLOGO)
        self._tweet(newton, PRIMEIRALEI)
        self._tweet(newton, GRAVITACAO)
        self._tweet(einstein, 'E = mc2')
        self._tweet(einstein, INSANIDADE)
        self._assert_tweets_home(descartes, [PENSOLOGO])
        self._assert_tweets_home(newton, [GRAVITACAO, PRIMEIRALEI, PENSOLOGO])
        self._assert_tweets_home(einstein, [INSANIDADE, 'E = mc2', GRAVITACAO, PRIMEIRALEI, PENSOLOGO])
        self._assert_tweets_home(anon, [INSANIDADE, 'E = mc2', GRAVITACAO, PRIMEIRALEI, PENSOLOGO])
        self._assert_tweets_user(anon, 'einstein', [INSANIDADE, 'E = mc2'])
        self._assert_tweets_user(newton, 'einstein', [INSANIDADE, 'E = mc2'])

    def _toggle_follow(self, client, username, value):
        r = client.post('/api/toggle_follow', {'username': username, 'value': value})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _tweet(self, client, content):
        r = client.post('/api/tweet', {'content': content})
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _assert_tweets_home(self, client, expected_tweets):
        r = client.get('/api/list_tweets')
        self.assertEqual(r.status_code, 200)
        tweets = json.loads(r.content.decode('utf-8'))
        tweets = tweets['tweets']
        actual_tweets = [t['content'] for t in tweets]
        self.assertEquals(actual_tweets, expected_tweets)

    def _assert_tweets_user(self, client, username, expected_tweets):
        r1 = client.get('/api/list_tweets', {'username': username})
        r2 = client.get('/api/get_user_details', {'username': username})
        self.assertEqual(r1.status_code, 200)
        self.assertEqual(r2.status_code, 200)
        tweets = json.loads(r1.content.decode('utf-8'))
        tweets = tweets['tweets']
        user_details = json.loads(r2.content.decode('utf-8'))
        actual_tweets = [t['content'] for t in tweets]
        self.assertEquals(actual_tweets, expected_tweets)
        for k in ['username', 'author_avatar', 'last_tweet', 'is_following']:
            self.assertIsNotNone(user_details[k])
