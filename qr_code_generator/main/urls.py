from django.conf.urls import include, url
from main.views import hello, article

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^article/(\d+)', article, name='article')
]
