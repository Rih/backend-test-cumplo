# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from io import BytesIO
from PIL import Image
import json
from account.factories import UserAccountFactory
from api.factories import INaturalistSettingsFactory
from api.bl.inaturalist import INaturalist
from api.models import INaturalistSettings
from django.urls import reverse
from django.db.models import Q
from django.test import TestCase, tag
from django.test.utils import override_settings
from rest_framework.test import APIClient
from django.conf import settings
import os


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
        self.auth_code = '8f80edb0349811ca0a4ff7f0e2e2aa85669118d5df083c7c792fdce1fd9ce538'
        self.token = '6985ab3317f65dcefc7d35ea2879990084995310e8d9cc568c19b0b1a57358c9'
        self.client = APIClient()

    @tag('oauth_auth_code_url')
    def test_inaturalist_oauth_auth_code_url(self):
        # python3.7 manage.py test --tag=oauth_auth_code_url
        # python3.7 manage.py test api.tests.INaturalistTest.test_inaturalist_oauth_auth_code_url
        res = INaturalist().get_auth_code_url()
        print(res)
        self.assertTrue(res.index('response_type=code') != -1)


    @tag('oauth_set_auth_code')
    def test_inaturalist_oauth_set_auth_code(self):
        # python3.7 manage.py test --tag=oauth_set_auth_code
        # python3.7 manage.py test api.tests.INaturalistTest.test_inaturalist_oauth_set_auth_code
        inat = INaturalist().set_auth_code('auth_test')
        self.assertTrue(isinstance(inat, INaturalistSettings))
        self.assertTrue(inat.auth_code, 'auth_test')

    @tag('oauth_get_auth_code')
    def test_inaturalist_oauth_get_token(self):
        # python3.7 manage.py test --tag=oauth_get_token
        # python3.7 manage.py test api.tests.INaturalistTest.test_inaturalist_oauth_get_token
        inat = INaturalistSettingsFactory.create(
            auth_code=self.auth_code
        )
        res = INaturalist().get_oauth_token()
        print(res)
        import pdb; pdb.set_trace()
        self.assertTrue(isinstance(res, str))

    @tag('oauth_get_latest_obs')
    def test_inaturalist_oauth_get_latest_observations(self):
        # python3.7 manage.py test --tag=oauth_get_latest_obs
        # python3.7 manage.py test api.tests.INaturalistTest.test_inaturalist_oauth_get_latest_observations
        inat = INaturalistSettingsFactory.create(
            auth_code=self.auth_code,
            token=self.token,
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

