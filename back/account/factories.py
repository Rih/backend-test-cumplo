import factory
from factory import SubFactory
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = 'John2'
    last_name = 'Doe2'
    username = 'user2'
    email = 'email@test.cl'
