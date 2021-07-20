# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from io import BytesIO
from PIL import Image
import json
from account.factories import UserAccountFactory
from api.models import INaturalistSettings
from api.bl.bigquery import BigQuery
from django.test import TestCase, tag
from django.test.utils import override_settings
from rest_framework.test import APIClient
from django.conf import settings
import os


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    MEDIA_ROOT='/app/test_media/',
)
class BigqueryTest(TestCase):

    fixtures = []

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' manage.py test api
        '''
        self.user = UserAccountFactory(username='test@test.com', email='test@test.com')
        self.user.set_password('pass')
        self.user.save()
        self.client.login(username='test@xstock.com', password='pass')
        self.client = APIClient()

    @tag('bigquery_select')
    def test_bigquery_select(self):
        # python3.7 manage.py test --tag=bigquery_select
        # python3.7 manage.py test api.tests.tests_bigquery.BigqueryTest.test_bigquery_select
        page = 0
        res = {'has_next': True}
        while res['has_next']:
            res = BigQuery(user_id=self.user.id).select(page)
            print(res['total_current'], res['has_next'])
            page = page + 1

    @tag('bigquery_insert')
    def test_bigquery_insert(self):
        # python3.7 manage.py test --tag=bigquery_insert
        # python3.7 manage.py test api.tests.tests_bigquery.BigqueryTest.test_bigquery_insert
        gps = {
            'ne': {
                'lat': 10.6,
                'lng': 10.3
            },
            'sw': {
                'lat': 10.6,
                'lng': 10.3
            }
        }
        result_api = {'result': 'here', 'a': [{'b': 1}]}
        res = BigQuery(user_id=self.user.id).insert(gps, result_api)
        self.assertTrue(res)
