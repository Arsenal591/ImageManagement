from django.conf.urls import url

from . import views, auth_views
from images.views import pic

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^authenticate/$', auth_views.authenticate, name='authenticate'),
    url(r'^signup/?$', auth_views.signup, name='signup'),
    url(r'^signup/submit/$', auth_views.signup_submit, name='signup-submit'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^changepassword/$', auth_views.changepassword, name='changepassword'),
    url(r'^changepassword/submit/$', auth_views.changepassword_submit, name='changepassword-submit'),
    url(r'^changeinfo/$', auth_views.changeinfo, name='changeinfo'),
    url(r'^changeinfo/submit/$', auth_views.changeinfo_submit, name='changeinfo-submit'),
    url(r'^managerelationship/$', views.manage_relationship, name='manage-relationship'),
    url(r'^users/(?P<visited_username>[A-Za-z0-9\@\.\+\-\_]+)/$', views.visit_user, name='visit-user'),
    url(r'^(?P<url>.*)unfollow/(?P<unfollow_username>[A-Za-z0-9\@\.\+\-\_]+)/$',views.unfollow_user, name='unfollow-user'),
    url(r'^(?P<url>.*)follow/(?P<follow_username>[A-Za-z0-9\@\.\+\-\_]+)/$', views.follow_user, name='follow-user'),
    url(r'^(?P<url>.*)unblack/(?P<unblack_username>[A-Za-z0-9\@\.\+\-\_]+)/$',views.unblack_user, name='unblack-user'),
    url(r'^(?P<url>.*)black/(?P<black_username>[A-Za-z0-9\@\.\+\-\_]+)/$',views.black_user, name='black-user'),
    url(r'^search_user/$',views.search_user, name='search-user'),
    url(r'^(?P<url>.*)unlike/(?P<image_id>\d+)/$', views.unlike, name='unlike'),
    url(r'^(?P<url>.*)uncollect/(?P<image_id>\d+)/$', views.uncollect, name='uncollect'),
    url(r'^(?P<url>.*)like/(?P<image_id>\d+)/$', views.like, name='like'),
    url(r'^(?P<url>.*)collect/(?P<image_id>\d+)/$', views.collect, name='collect'),
    url(r'^(?P<url>.*)comment/(?P<image_id>\d+)/$', views.comment, name='comment'),
    url(r'^pic/([1-9][0-9]*)/$', pic, name='pic'),
    url(r'^profile/$', views.profile, name='profile'),
]
