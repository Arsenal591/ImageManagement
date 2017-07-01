from django.conf.urls import url

from . import views, auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/', auth_views.login, name='login'),
    url(r'^authenticate', auth_views.authenticate, name='authenticate'),
    url(r'^signup/$', auth_views.signup, name='signup'),
    url(r'^signup/submit', auth_views.signup_submit, name='signup-submit'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^changepassword/$', auth_views.changepassword, name='changepassword'),
    url(r'^changepassword/submit', auth_views.changepassword_submit, name='changepassword-submit'),
    url(r'^changeinfo/$', auth_views.changeinfo, name='changeinfo'),
    url(r'^changeinfo/submit', auth_views.changeinfo_submit, name='changeinfo-submit'),
]