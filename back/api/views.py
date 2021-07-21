# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django libs
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
# Own libs
from django.contrib.auth import get_user_model
from account.models import UserProfile
from api.bl.inaturalist import INaturalist
from api.bl.bigquery import BigQuery
# Create your views here.


class ObservationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        results = BigQuery(user_id=request.user.id).select(int(page))
        return Response(results)

    def post(self, request, *args, **kwargs):
        results = INaturalist().get_latest_obs(request.data['gps'])
        audit = BigQuery(
            user_id=request.user.id
        ).insert(request.data['gps'], results)
        return Response({'results': results, 'audit': audit})


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


class INaturalistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if kwargs['mode'] == 'request':  # step 1
            return Response(
                {'url': INaturalist().get_auth_code_url()},
                status=status.HTTP_200_OK
            )
        if kwargs['mode'] == 'token' and code:  # step 2
            return Response(
                {
                    'code': code,
                    'tkn': INaturalist().get_oauth_token(code)
                },
                status=status.HTTP_200_OK
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
