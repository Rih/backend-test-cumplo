# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Standard libs
# Own libs
from account.bl.recaptcha import validate_captcha
from account.tests.mocks import RequestMock, RECAPTCHA_RESPONSE
# Django libs
from unittest.mock import patch
from django.test import SimpleTestCase
from django.test.utils import override_settings, tag


@tag('recaptcha')
@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    ENVIRONMENT='UNIT_TESTING'
)
class RecaptchaTest(SimpleTestCase):

    fixtures = []

    @tag('validate_recaptcha_success')
    @patch('requests.post')
    def test_validate_recaptcha_success(self, request_mock):
        # python3.7 manage.py test --tag=validate_recaptcha_success
        request_mock.return_value = RequestMock(
            mode='success',
            response=RECAPTCHA_RESPONSE,
        )
        res = validate_captcha('CLIENT_TOKEN')
        self.assertTrue(res['success'])
        self.assertEqual(res['client_token'], 'CLIENT_TOKEN')

    @tag('validate_recaptcha_fail')
    @patch('requests.post')
    def test_validate_recaptcha_fail(self, request_mock):
        # python3.7 manage.py test --tag=validate_recaptcha_fail
        request_mock.return_value = RequestMock(
            mode='fail',
            response=RECAPTCHA_RESPONSE,
        )
        res = validate_captcha('CLIENT_TOKEN')
        self.assertTrue(not(res['success']))
        self.assertEqual(res['client_token'], 'CLIENT_TOKEN')
