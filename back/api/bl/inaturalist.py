# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
# Django libs
from django.conf import settings
from urllib.parse import urlencode
from api.models import INaturalistSettings


class INaturalist:

    def __init__(self, **kw):
        self.client_id = kw.get('cid', settings.INAT_CLIENT_ID)
        self.base_url = kw.get('base_url', settings.INAT_BASE_URL)
        self.redirect_url = kw.get('redirect', settings.INAT_REDIRECT_URL)

    def get_header(self, tkn: str = None):
        header = {
            # 'Content-Type': 'application/json',
        }
        if tkn:
            header.update({'Authorization': f'Bearer {tkn}'})
        return header

    def get_auth_code_url(self) -> str:
        query_params = urlencode({
            'client_id': settings.INAT_CLIENT_ID,
            'redirect_uri': self.redirect_url,
            'response_type': 'code'
        })
        url = f'{self.base_url}/oauth/authorize?{query_params}'
        return url

    def get_inat_settings(self) -> str:
        inat = INaturalistSettings.objects.filter(expired=False).last()
        return inat

    def set_auth_code(self, code: str) -> INaturalistSettings:
        INaturalistSettings.objects.filter(expired=False).update(expired=True)
        isettings = INaturalistSettings.objects.create(
            auth_code=code
        )
        return isettings

    def get_oauth_token(self) -> str:
        inat = self.get_inat_settings()
        url = f'{self.base_url}/oauth/token'
        payload = {
            'client_id': settings.INAT_CLIENT_ID,
            'client_secret': settings.INAT_SECRET,
            'code': inat.auth_code,
            'redirect_uri': self.redirect_url,
            'grant_type': 'authorization_code',
        }
        res = requests.post(url, payload)
        if res.status_code != 200:
            inat.expired = True
            inat.save()
            return None
        result = res.json()
        inat.token = result.get('access_token')
        inat.save()
        return result.get('access_token')

    def get_latest_obs(self, gps: dict) -> list:
        inat = self.get_inat_settings()
        url = f'{self.base_url}/observations.json'
        head = self.get_header(inat.token)
        payload = {
            'page': 0,
            'per_page': settings.INAT_PER_PAGE,
            'order_by': 'date_added',
            'swlat': gps['sw']['lat'],
            'swlng': gps['sw']['lng'],
            'nelat': gps['ne']['lat'],
            'nelng': gps['ne']['lng']
        }
        res = requests.get(url, payload)
        return res.json()
