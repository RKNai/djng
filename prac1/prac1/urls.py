from django.conf.urls import patterns, include, url
from gotapi.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    url(r'^characterpage/$', characterpage),
    url(r'^housepage/$', housepage),
    url(r'^placepage/$', placepage),
    # url(r'^character/(\w+)/$', characterpadge),
    # url(r'^$', 'prac1.views.home', name='home'),
    # url(r'^prac1/', include('prac1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

