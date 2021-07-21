from django.urls import include, path
from account.views import UserCreationView
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'account'
urlpatterns = [
    # user
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path(
        'signup/',
        UserCreationView.as_view(),
        name='account_creation'
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
