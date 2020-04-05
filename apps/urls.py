from django.conf.urls import url
from django.urls import path
from apps.views import Generate


urlpatterns = [
    path('generate/', Generate.as_view(), name="generate"),
]