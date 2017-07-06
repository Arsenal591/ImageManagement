from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'upload_batch', views.upload_batch, name='upload_batch'),
    url(r'^pool$', views.img_pool, name='pool'),
    url(r'process/([1-9][0-9]*)$', views.process, name='process'),
    url(r'detail/([1-9][0-9]*)$', views.detail, name='detail'),
    url(r'^filter$', views.filtershow, name='filter'),    
    url(r'^pic/([1-9][0-9]*)$', views.pic, name='pic'),
    url(r'^search_img$', views.searchimg, name='searchimg'),
    url(r'^searchbar$', views.searchbar, name='searchbar'),
    url(r'^del_pic/([1-9][0-9]*)$', views.del_pic, name='del_pic'),
]
