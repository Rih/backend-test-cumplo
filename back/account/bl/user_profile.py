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


def transform_data(data):
    return {
        'first_name': data['firstname'],
        'last_name': data['lastname'],
        'password': make_password(data['password']),
        'email': data['username'],
        'username': data['username'],
    }
