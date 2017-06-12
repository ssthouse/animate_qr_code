from django.conf.urls import include, url
from main.views import hello, article, crudops

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^article/(\d+)', article, name='article'),
    url(r'^test_db/', crudops, name='test_db')
]
