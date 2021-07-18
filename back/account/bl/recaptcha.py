import requests
from django.conf import settings
import json

RECAPTCHA_TEST = 'tokenCaptcha123'


def validate_captcha(client_token):
    response = requests.post(
        settings.DRF_RECAPTCHA_VERIFY_ENDPOINT,
        {
            'secret': settings.DRF_RECAPTCHA_SECRET_KEY,
            'response': client_token
        }
    )
    resp = json.loads(response.content)
    resp.update({'client_token': client_token})
    return resp
