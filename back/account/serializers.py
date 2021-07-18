# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from account.data import RECAPTCHA_MIN_SCORE


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):


    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['pk'] = user.pk
        token['email'] = user.email
        token['last_name'] = user.last_name
        token['first_name'] = user.first_name
        token['username'] = user.username
        # token['recaptcha'] = cls.recaptchaToken
        return token

    def validate(self, attrs, **kwargs):
        # The default result (access/refresh tokens)
        attrs['email'] = attrs['username']
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        response = kwargs.get('recaptcha_result')
        if not response['success'] or response['score'] < RECAPTCHA_MIN_SCORE:
            del data['access']
            del data['refresh']

        data.update({'recaptcha': response})
        # and everything else you want to send in the response
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Scafold serializer User
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'is_staff']


class UserCreationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'password']


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

