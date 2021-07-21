# -*- coding: utf-8 -*-
# Standard libs
import logging
# Django libs
from django.db import models
from django.contrib.auth import get_user_model
from api.models import Apimodel
# Own libs
from account.data import AVATAR_URL, AVATAR_OPTS
from account.bl import utils

log = logging.getLogger(__name__)

# Create your models here.


class UserProfile(Apimodel):
    DEFAULT_AVATAR = f'{AVATAR_URL}?{utils.to_queryparams(AVATAR_OPTS)}'
    picture = models.TextField(default=DEFAULT_AVATAR)
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE
    )
