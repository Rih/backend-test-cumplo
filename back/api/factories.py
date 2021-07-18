import factory
from factory import SubFactory
from api.models import INaturalistSettings


class INaturalistSettingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = INaturalistSettings

    auth_code = 'auth'
    token = 'tkn'
    expired = False
