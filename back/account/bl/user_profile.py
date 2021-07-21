# -*- coding: utf-8 -*-
# Django libs
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()

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


def get_data(mode, data):
    new_data = data.copy()
    if mode in ['password']:
        new_data['password'] = make_password(new_data['password'])
    if mode == 'creation':
        new_data['first_name'] = new_data['firstname']
        new_data['last_name'] = new_data['lastname']
        new_data['password'] = make_password(new_data['password'])
        new_data['email'] = new_data['username']
        del new_data['lastname']
        del new_data['firstname']
    return new_data
