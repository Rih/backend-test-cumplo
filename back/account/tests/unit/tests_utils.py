# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Standard libs
# Own libs
from account.bl import utils
# Django libs
from django.test import SimpleTestCase
from django.test.utils import override_settings, tag


@override_settings(
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage',
    EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    MEDIA_ROOT='/app/test_media/',
    ENVIRONMENT='UNIT_TESTING'
)
class UtilsTest(SimpleTestCase):

    fixtures = []

    @tag('to_queryparams')
    def test_utils_to_queryparams(self):
        # python3.7 manage.py  test --tag=to_queryparams
        # trim blank spaces case
        res = utils.to_queryparams({' a': 1, 'b ': 2})
        self.assertEquals(res, 'a=1&b=2')
        # empty case
        res = utils.to_queryparams({})
        self.assertEquals(res, '')
        # valid case
        res = utils.to_queryparams({'a': 1, 'b': 2})
        self.assertEquals(res, 'a=1&b=2')
