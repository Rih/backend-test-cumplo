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
from django.test.utils import override_settings, tag
from rest_framework.test import APITestCase, APIClient
from django.conf import settings
import os


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    MEDIA_ROOT='/app/test_media/',
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

    @tag('api_get_latest_obs')
    def test_api_get_latest_observations(self):
        # python3.7 manage.py test --tag=oauth_get_latest_obs
        # python3.7 manage.py test api.tests.tests_api.ApiTest.test_api_get_latest_observations
        inat = INaturalistSettingsFactory.create(
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
        import pdb; pdb.set_trace()
        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result) == 1)
        self.assertTrue("thumb_url" in result[0]['photos'][0])

