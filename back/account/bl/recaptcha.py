# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.conf import settings


def validate_captcha(client_token):
    response = requests.post(
        settings.DRF_RECAPTCHA_VERIFY_ENDPOINT,
        {
            'secret': settings.DRF_RECAPTCHA_SECRET_KEY,
            'response': client_token
        }
    )
    resp = response.json()
    resp.update({'client_token': client_token})
    return resp
