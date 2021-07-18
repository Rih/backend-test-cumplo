# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django libs
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
# Own libs
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from account.models import UserProfile
from api.bl.inaturalist import INaturalist
# Create your views here.


class ObservationsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        results = INaturalist().get_latest_obs(request.data['gps'])
        return Response(results)


class ProfilePicView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        User = get_user_model()
        avatar = request.data['obs']
        user = User.objects.get(pk=request.user.pk)
        try:
            profile = user.profile
            profile.picture = avatar
            profile.save()
        except User.profile.RelatedObjectDoesNotExist:
            UserProfile.objects.create(
                picture=avatar,
                user=user
            )
        return Response(status=status.HTTP_200_OK)
