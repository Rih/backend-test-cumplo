# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from account.serializers import (
    MyTokenObtainPairSerializer,
    UserCreationModelSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from account.bl import user_profile, recaptcha


User = get_user_model()


# returns { refresh, access, recaptcha }
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = recaptcha.validate_captcha(request.data.get('recaptchaToken'))
        tokens = MyTokenObtainPairSerializer(request.data).validate(
            request.data,
            recaptcha_result=response
        )
        return Response(tokens, status=status.HTTP_200_OK)


class UserCreationView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserCreationModelSerializer

    # tested at tests.test_api_account_post_creation
    def post(self, request, *args, **kwargs):
        response = recaptcha.validate_captcha(request.data.get('recaptchaToken'))
        data = user_profile.get_data('creation', request.data)
        serializer = UserCreationModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            result = request.data.copy()
            tokens = MyTokenObtainPairSerializer(result).validate(
                result,
                recaptcha_result=response
            )
            result.update(tokens)
            del result['password']
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
