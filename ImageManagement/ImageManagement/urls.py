"""
Definition of urls for ImageManagement.
"""

from django.conf.urls import include, url
from django.contrib import admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', ImageManagement.views.home, name='home'),
    # url(r'^ImageManagement/', include('ImageManagement.ImageManagement.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('users.urls')),
    url(r'^', include('images.urls')),
    #url(r'^', include('users.urls')),
]
