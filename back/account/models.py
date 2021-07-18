# -*- coding: utf-8 -*-
# Standard libs
import logging
# Django libs
from django.db import models
from django.contrib.auth import get_user_model
from api.models import Apimodel
# Own libs

log = logging.getLogger(__name__)

# Create your models here.


class UserProfile(Apimodel):
    DEFAULT_AVATAR = 'https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light'
    picture = models.TextField(default=DEFAULT_AVATAR)
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE
    )

