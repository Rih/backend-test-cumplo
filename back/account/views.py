from django.shortcuts import render
from account.serializers import (
    MyTokenObtainPairSerializer,
    UserSerializer,
    UserModelSerializer,
    UserCreationModelSerializer
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from account.bl import user_profile, recaptcha, role

# Create your views here.


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


class UserModelView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserModelSerializer

    def get_object(self):
        try:
            return User.objects.get(pk=self.request.user.pk)
        except User.DoesNotExist:
            raise Http404


class UserDetail(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('pk')) if kwargs.get('pk') else self.get_object(request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
