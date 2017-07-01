from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload$', views.upload, name='upload'),
    url(r'^pool$', views.img_pool, name='pool'),
    url(r'process/([1-9][0-9]*)$', views.process, name='process')
]
