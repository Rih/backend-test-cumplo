from django.urls import path
from api.views import (
    AuditObservationsView,
    ObservationsView,
    ProfilePicView,
    INaturalistView,
)
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'api'
urlpatterns = [
    path(
        'audit/',
        AuditObservationsView.as_view(),
        name='audit'
    ),
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
    path(
        'inaturalist/<str:mode>/',
        INaturalistView.as_view(),
        name='inaturalist'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
