from django.conf.urls import include, url
from main.views import hello, article, crudops, connect, login

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^article/(\d+)', article, name='article'),
    url(r'^test_db/', crudops, name='test_db'),
    url(r'^connect/', connect, name='connect'),
    url(r'^login/', login, name='login'),
]
