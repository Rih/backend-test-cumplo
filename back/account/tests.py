# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Standard libs
from io import BytesIO
from PIL import Image
import json
import os
# Own libs
from account.factories import UserAccountFactory
from account.data import GENDER_OPTIONS, USER_TYPES
# Django libs
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test.utils import override_settings
from rest_framework.test import APITestCase, APIClient
from django.conf import settings
from django.core.files.base import File


User = get_user_model()


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    MEDIA_ROOT='/app/test_media/',
    ENVIRONMENT='UNIT_TESTING'
)
class AccountTest(APITestCase):

    fixtures = []

    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def setUp(self):
        ''' Check coverage
            coverage3 run --source='.' backend/manage.py test account
        '''
        self.user = UserAccountFactory(username='test@test.com', email='test@test.com')
        self.user1 = UserAccountFactory(
            username='drigox90rih@gmail.com',
            email='drigox90rih@gmail.com'
        )
        self.user.set_password('pass')
        self.user.save()
        self.user1.set_password('pass1')
        self.user1.save()
        self.client.login(username='test@test.com', password='pass')
        self.client = APIClient()

    def test_api_user_get_correct(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_user_get_correct
        '''
        url = reverse('account:users', kwargs={'pk': self.user.pk})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(200, response.status_code)
        self.assertEquals('test@test.com', data.get('username'))
        self.assertEquals('test@test.com', data.get('email'))

    def test_api_get_user(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_get_user
        '''
        url = reverse('account:users', kwargs={'pk': 0})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals('test@test.com', data.get('username'))
        self.assertEquals('test@test.com', data.get('email'))
        self.assertEquals('John2', data.get('first_name'))
        self.assertEquals('Doe2', data.get('last_name'))

    def test_api_user_get_not_found(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_user_get_not_found
        '''
        url = reverse('account:users', kwargs={'pk': 9999})
        self.client.force_authenticate(self.user)
        response = self.client.get(
            url,
            content_type='application/json'
        )
        data = json.loads(response.content)
        self.assertEquals(404, response.status_code)
        self.assertEquals('No encontrado.', data.get('detail'))

    def test_api_account_post_creation(self):
        '''
        python3.7 manage.py test account.tests.AccountTest.test_api_account_post_creation
        '''
        url = reverse('account:account_creation')
        email = 'drigox90rih@create.com'  # test@xstock.new
        response = self.client.post(
            url,
            json.dumps({
                'email': email,
                'first_name': 'Rod',
                'last_name': 'Gar',
                'password': 'pass_valid',
            }),
            content_type='application/json'
        )
        data = json.loads(response.content)
        print(data)
        self.assertEquals(201, response.status_code)
        self.assertEquals(email, data.get('username'))
        self.assertEquals(email, data.get('email'))
        self.assertEquals('Rod', data.get('first_name'))
        self.assertEquals('Gar', data.get('last_name'))
        user = User.objects.get(email='drigox90rih@gmail.com')
        roles = [g.name for g in user.groups.all()]

