# -*- coding: utf-8 -*-
# Django libs
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import Http404

# Own libs


def existing_user(**kwargs):
        try:
            if kwargs.get('email'):
                return User.objects.get(
                    email=kwargs.get('email'),
                )
            if kwargs.get('username'):
                return User.objects.get(
                    email=kwargs.get('username'),
                )
            return None
        except User.DoesNotExist:
            if kwargs.get('throw404'):
                raise Http404
            return None


def get_data(type, data):
    new_data = data.copy()
    if type in ['password', 'validate', 'creation', 'recovery']:
        new_data['password'] = make_password(new_data['password'])
    if type == 'creation':
        new_data['username'] = new_data['email']
    return new_data



