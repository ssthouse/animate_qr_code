from django.conf.urls import include, url
from main.views import hello

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
]
