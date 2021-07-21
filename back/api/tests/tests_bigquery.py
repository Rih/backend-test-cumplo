# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from account.factories import UserAccountFactory
from api.bl.bigquery import BigQuery
from django.test import TestCase, tag
from django.test.utils import override_settings
from unittest.mock import patch
from api.tests.mocks import bquerymock


@tag('bigquery')
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
        self.user = UserAccountFactory(
            username='test@test.com',
            email='test@test.com'
        )
        self.user.set_password('pass')
        self.user.save()

    @tag('bigquery_select')
    @patch('api.bl.bigquery.BigQuery.get_client')
    def test_bigquery_select(self, bq_mock):
        # python3.7 manage.py test --tag=bigquery_select
        # python3.7 manage.py test api.tests.tests_bigquery.BigqueryTest.test_bigquery_select
        page = 0
        res = {'hasNext': True}
        bq_mock.return_value = bquerymock().Client()
        res = BigQuery(user_id=self.user.id).select(page)
        print(res, res['hasNext'])

    @tag('bigquery_insert_success')
    @patch('api.bl.bigquery.BigQuery.get_client')
    def test_bigquery_insert_success(self, bq_mock):
        # python3.7 manage.py test --tag=bigquery_insert
        # python3.7 manage.py test api.tests.tests_bigquery.BigqueryTest.test_bigquery_insert
        bq_mock.return_value = bquerymock(insert=True).Client()
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

    @tag('bigquery_insert_failed')
    @patch('api.bl.bigquery.BigQuery.get_client')
    def test_bigquery_insert_failed(self, bq_mock):
        # python3.7 manage.py test --tag=bigquery_insert
        # python3.7 manage.py test api.tests.tests_bigquery.BigqueryTest.test_bigquery_insert
        bq_mock.return_value = bquerymock(insert=False).Client()
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
        self.assertTrue(not(res))
