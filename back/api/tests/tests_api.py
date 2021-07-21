# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from account.factories import UserAccountFactory
from api.factories import INaturalistSettingsFactory
from django.urls import reverse
from unittest.mock import patch
from account.tests.mocks import RequestMock
from api.tests.mocks import bquerymock, API_RESPONSE
from django.test.utils import override_settings, tag
from rest_framework.test import APITestCase, APIClient
from django.conf import settings


@tag('api')
@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    MEDIA_ROOT='/app/test_media/',
    INAT_PER_PAGE=1,
)
class ApiTest(APITestCase):

    fixtures = []

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test api
        '''
        self.user = UserAccountFactory(username='test@test.com', email='test@test.com')
        self.user.set_password('pass')
        self.user.save()
        self.client.login(username='test@xstock.com', password='pass')
        self.auth_code = '8f80edb0349811ca0a4ff7f0e2e2aa85669118d5df083c7c792fdce1fd9ce538'
        self.token = '6985ab3317f65dcefc7d35ea2879990084995310e8d9cc568c19b0b1a57358c9'
        self.client = APIClient()

    @tag('api_get_observations_audit')
    @patch('api.bl.bigquery.BigQuery.get_client')
    def test_api_get_observations_audit(self, bq_mock):
        # python3.7 manage.py test --tag=api_get_observations_audit
        bq_mock.return_value = bquerymock().Client()
        url = reverse('api:observations')
        params = {'page': 1}
        self.client.force_authenticate(self.user)
        res = self.client.get(
            url,
            params=params,
            content_type='application/json'
        )
        result = json.loads(res.content)
        self.assertListEqual(
            ['data', 'hasPrev', 'hasNext', 'current', 'perPage', 'totalCurrent', 'total'],
            list(result.keys())
        )
        self.assertTrue(len(result['data']) > 0)

    @tag('api_post_latest_obs')
    @patch('requests.get')
    @patch('api.bl.bigquery.BigQuery.get_client')
    def test_api_post_latest_observations(self, bq_mock, req_mock):
        # python3.7 manage.py test --tag=api_post_latest_obs
        # python3.7 manage.py test api.tests.tests_api.ApiTest.test_api_post_latest_observations
        bq_mock.return_value = bquerymock().Client()
        req_mock.return_value = RequestMock(
            mode='success',
            response=API_RESPONSE['observation']
        )
        INaturalistSettingsFactory.create(
            auth_code=self.auth_code,
            token=self.token,
        )
        url = reverse('api:observations')
        gps = {
            'ne': {
                'lat': -39.80847010729648,
                'lng': -73.18482398986818,
            },
            'sw': {
                'lat': -39.84142929280931,
                'lng': -73.23220252990724,
            }
        }
        payload = {'gps': gps}
        self.client.force_authenticate(self.user)
        res = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        result = json.loads(res.content)
        self.assertListEqual(['results', 'audit'], list(result.keys()))
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(isinstance(result['results'], list))
        self.assertTrue(result['audit'])
        self.assertTrue(len(result['results']) == settings.INAT_PER_PAGE)
        self.assertTrue("thumb_url" in result['results'][0]['photos'][0])

    @tag('api_post_assign_obs')
    def test_api_post_assign_obs(self):
        # python3.7 manage.py test --tag=api_post_assign_obs
        # python3.7 manage.py test api.tests.tests_api.ApiTest.test_api_post_assign_obs
        INaturalistSettingsFactory.create(
            auth_code=self.auth_code,
            token=self.token,
        )
        url = reverse('api:profile')
        avatar_url = 'http://url.image-thumb.com/img.png'
        payload = {'obs': avatar_url}
        self.client.force_authenticate(self.user)
        res = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(200, res.status_code)
        profile = self.user.profile
        self.assertEqual(profile.picture, avatar_url)

    @tag('api_get_inat_request_code_url')
    def test_api_get_inat_request_code(self):
        # python3.7 manage.py test --tag=api_get_inat_request_code_url
        # python3.7 manage.py test api.tests.tests_api.ApiTest.test_api_get_inat_request_code
        url = reverse('api:inaturalist', kwargs={'mode': 'request'})
        self.client.force_authenticate(self.user)
        res = self.client.get(
            url,
            content_type='application/json'
        )
        self.assertEqual(200, res.status_code)
        result = json.loads(res.content)
        self.assertTrue(result['url'].index('response_type=code') != -1)

    @tag('api_get_oauth_token')
    @patch('requests.post')
    def test_api_get_oauth_token(self, req_mock):
        # python3.7 manage.py test --tag=api_get_oauth_token
        req_mock.return_value = RequestMock(
            mode='success',
            status=200,
            response=API_RESPONSE['token']
        )
        url = reverse('api:inaturalist', kwargs={'mode': 'token'})
        self.client.force_authenticate(self.user)
        res = self.client.get(
            f'{url}?code=the_code',
            content_type='application/json'
        )
        self.assertEqual(200, res.status_code)
        result = json.loads(res.content)
        self.assertTrue(result['code'], 'the_code')
        url = reverse('api:inaturalist', kwargs={'mode': 'invalid_mode'})
        res = self.client.get(
            url,
            content_type='application/json'
        )
        # invalid get params
        self.assertEqual(400, res.status_code)
