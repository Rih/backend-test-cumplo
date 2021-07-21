# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Standard libs
import json
# Own libs
from account.factories import UserAccountFactory
from account.tests.mocks import RequestMock, RECAPTCHA_RESPONSE
# Django libs
from django.contrib.auth import get_user_model
from django.urls import reverse
from unittest.mock import patch
from django.test.utils import override_settings, tag
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


@tag('account')
@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    ENVIRONMENT='UNIT_TESTING'
)
class AccountTest(APITestCase):

    fixtures = []

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' backend/manage.py test account
        '''
        self.user = UserAccountFactory(
            username='test@test.com',
            email='test@test.com'
        )
        self.user.set_password('pass')
        self.user.save()
        self.client = APIClient()

    @tag('api_login_success')
    @patch('requests.post')
    def test_api_login_success(self, request_mock):
        # python3.7 manage.py test --tag=api_login_success
        request_mock.return_value = RequestMock(
            mode='success',
            response=RECAPTCHA_RESPONSE,
        )
        url = reverse('token_obtain_pair')
        payload = {
            'username': 'test@test.com',
            'password': 'pass',
            'recaptchaToken': 'TOKN_FAKE'
        }
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertTrue(len(data['refresh']) > 0)
        self.assertTrue(len(data['access']) > 0)
        self.assertTrue(data['recaptcha']['success'])
        self.assertTrue(data['recaptcha']['client_token'], 'TOKN_FAKE')

    @tag('api_login_failed')
    @patch('requests.post')
    def test_api_login_failed(self, request_mock):
        # python3.7 manage.py test --tag=api_login_failed
        request_mock.return_value = RequestMock(
            mode='fail',
            response=RECAPTCHA_RESPONSE,
        )
        url = reverse('token_obtain_pair')
        payload = {
            'username': 'test@test.com',
            'password': 'pass',
            'recaptchaToken': 'TOKN_FAKE'
        }
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertTrue('refresh' not in data)
        self.assertTrue('access' not in data)
        self.assertTrue(not(data['recaptcha']['success']))
        self.assertTrue(data['recaptcha']['client_token'], 'TOKN_FAKE')

    @tag('api_login_less_score')
    @patch('requests.post')
    def test_api_login_less_score(self, request_mock):
        # python3.7 manage.py test --tag=api_login_less_score
        request_mock.return_value = RequestMock(
            mode='less_score',
            response=RECAPTCHA_RESPONSE,
        )
        url = reverse('token_obtain_pair')
        payload = {
            'username': 'test@test.com',
            'password': 'pass',
            'recaptchaToken': 'TOKN_FAKE'
        }
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertTrue('refresh' not in data)
        self.assertTrue('access' not in data)
        self.assertTrue(not (data['recaptcha']['success']))
        self.assertTrue(data['recaptcha']['client_token'], 'TOKN_FAKE')

    @tag('api_login_wrong_pass')
    @patch('requests.post')
    def test_api_login_wrong_pass(self, request_mock):
        # python3.7 manage.py test --tag=api_login_wrong_pass
        request_mock.return_value = RequestMock(
            mode='success',
            response=RECAPTCHA_RESPONSE,
        )
        url = reverse('token_obtain_pair')
        payload = {
            'username': 'test@test.com',
            'password': 'pass_bad',
            'recaptchaToken': 'TOKN_FAKE'
        }
        response = self.client.post(
            url,
            json.dumps(payload),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(401, response.status_code)
        self.assertTrue('refresh' not in data)
        self.assertTrue('access' not in data)
        self.assertTrue(data['detail'], 'No active account found with the given credentials')

    @tag('api_post_creation')
    @patch('requests.post')
    def test_api_account_post_creation(self, request_mock):
        # python3.7 manage.py test --tag=api_post_creation
        '''
        python3.7 manage.py test account.tests.integration.tests_account.AccountTest.test_api_account_post_creation
        '''
        request_mock.return_value = RequestMock(
            mode='success',
            response=RECAPTCHA_RESPONSE,
        )
        url = reverse('account:account_creation')
        email = 'drigox90rih@create.com'  # test@xstock.new
        response = self.client.post(
            url,
            json.dumps({
                'username': email,
                'firstname': 'Rod',
                'lastname': 'Gar',
                'password': 'pass_valid',
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(201, response.status_code)
        self.assertTrue('access' in data)
        self.assertTrue('refresh' in data)
        self.assertEquals(email, data.get('username'))
        self.assertEquals(email, data.get('email'))
        self.assertEquals('Rod', data.get('firstname'))
        self.assertEquals('Gar', data.get('lastname'))
        user = User.objects.get(email='drigox90rih@create.com')
        self.assertTrue(isinstance(user, User))

    @tag('api_post_creation_exists')
    @patch('requests.post')
    def test_api_account_post_creation_exists(self, request_mock):
        # python3.7 manage.py test --tag=api_post_creation_exists
        '''
        python3.7 manage.py test account.tests.integration.tests_account.AccountTest.test_api_account_post_creation_exists
        '''
        request_mock.return_value = RequestMock(
            mode='success',
            response=RECAPTCHA_RESPONSE,
        )
        url = reverse('account:account_creation')
        email = 'test@test.com'
        response = self.client.post(
            url,
            json.dumps({
                'username': email,
                'firstname': 'Rod',
                'lastname': 'Gar',
                'password': 'pass_valid',
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(400, response.status_code)
        self.assertTrue('access' not in data)
        self.assertTrue('refresh' not in data)
        self.assertTrue(isinstance(data['username'], list))
        self.assertListEqual(
            data['username'],
            ['Ya existe un usuario con este nombre.']
        )
