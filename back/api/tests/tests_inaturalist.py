# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Django libs
from rest_framework.test import APIClient
from django.test import TestCase, tag
from django.test.utils import override_settings
from unittest.mock import patch
# Own libs
from account.factories import UserAccountFactory
from account.tests.mocks import RequestMock
from api.factories import INaturalistSettingsFactory
from api.bl.inaturalist import INaturalist
from api.models import INaturalistSettings
from api.tests.mocks import API_RESPONSE


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    MEDIA_ROOT='/app/test_media/',
)
class INaturalistTest(TestCase):

    fixtures = []

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test api
        '''
        self.user = UserAccountFactory(username='test@test.com', email='test@test.com')
        self.user.set_password('pass')
        self.user.save()
        self.client.login(username='test@xstock.com', password='pass')
        self.auth_code = '17ffd9e5ebc183782358b8af35faa23d0bb68029f96d972a685898e1548ac395'
        self.token = '6985ab3317f65dcefc7d35ea2879990084995310e8d9cc568c19b0b1a57358c9'
        self.client = APIClient()

    @tag('oauth_get_header')
    def test_inaturalist_oauth_get_header(self):
        # python3.7 manage.py test --tag=oauth_get_header
        res = INaturalist().get_header()
        # simple case
        self.assertDictEqual(
            res,
            {'Content-Type': 'application/json'}
        )
        res = INaturalist().get_header('eyASDF')
        # auth case
        self.assertDictEqual(
            res,
            {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer eyASDF'
             }
        )

    @tag('oauth_auth_code_url')
    def test_inaturalist_oauth_auth_code_url(self):
        # python3.7 manage.py test --tag=oauth_auth_code_url
        auth_url = INaturalist().get_auth_code_url()
        print(auth_url)
        self.assertTrue(auth_url.index('response_type=code') != -1)

    @tag('oauth_set_auth_code')
    def test_inaturalist_oauth_set_auth_code(self):
        # python3.7 manage.py test --tag=oauth_set_auth_code
        inat = INaturalist().set_auth_code('auth_test')
        self.assertTrue(isinstance(inat, INaturalistSettings))
        self.assertTrue(inat.auth_code, 'auth_test')

    @tag('oauth_get_oauth_token')
    @patch('requests.post')
    def test_inaturalist_oauth_get_token(self, req_mock):
        # python3.7 manage.py test --tag=oauth_get_oauth_token
        # python3.7 manage.py test api.tests.tests_inaturalist.INaturalistTest.test_inaturalist_oauth_get_token
        INaturalistSettingsFactory.create(
            auth_code=self.auth_code
        )
        req_mock.return_value = RequestMock(
            mode='success',
            status=200,
            response=API_RESPONSE['token']
        )
        # case success
        res = INaturalist().get_oauth_token(self.auth_code)
        self.assertTrue(isinstance(res, str))
        req_mock.return_value = RequestMock(
            mode='failed',
            status=400,
            response=API_RESPONSE['token']
        )
        # case failed
        res = INaturalist().get_oauth_token(self.auth_code)
        self.assertTrue(res is None)

    @tag('oauth_get_latest_obs')
    @patch('requests.get')
    def test_inaturalist_oauth_get_latest_observations(self, req_mock):
        # python3.7 manage.py test --tag=oauth_get_latest_obs
        # python3.7 manage.py test api.tests.tests_inaturalist.INaturalistTest.test_inaturalist_oauth_get_latest_observations
        INaturalistSettingsFactory.create(
            auth_code=self.auth_code,
            token=self.token,
        )
        req_mock.return_value = RequestMock(
            mode='success',
            response=API_RESPONSE['observation']
        )
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
        res = INaturalist().get_latest_obs(gps)
        self.assertTrue(isinstance(res, list))
        self.assertTrue("thumb_url" in res[0]['photos'][0])
