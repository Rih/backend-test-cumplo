from django.urls import include, path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'
urlpatterns = [
    path(
        'observations/',
        ObservationsView.as_view(),
        name='observations'
    ),
    path(
        'profile/',
        ProfilePicView.as_view(),
        name='profile'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
