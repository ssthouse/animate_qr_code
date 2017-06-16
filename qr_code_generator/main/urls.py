from django.conf.urls import include, url
from main.views import hello, article, crudops, connect, login, index, submit_img, download_gif

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^article/(\d+)', article, name='article'),
    url(r'^test_db/', crudops, name='test_db'),
    url(r'^connect/', connect, name='connect'),
    url(r'^login/', login, name='login'),
    url(r'^index/', index, name='index'),
    url(r'^submit/', submit_img, name='submit'),
    url(r'^download', download_gif, name='download')
]
