from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload$', views.upload, name='upload'),
    url(r'upload_batch', views.upload_batch, name='upload_batch'),
    url(r'^pool$', views.img_pool, name='pool'),
    url(r'process/([1-9][0-9]*)$', views.process, name='process'),
    url(r'detail/([1-9][0-9]*)$', views.detail, name='detail'),
    url(r'^filter$', views.filtershow, name='filter'),    
    url(r'^home$', views.home),
]
