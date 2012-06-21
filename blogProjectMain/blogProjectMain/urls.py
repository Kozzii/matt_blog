from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
from blogProjectMain.views import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogProjectMain.views.home', name='home'),
    # url(r'^blogProjectMain/', include('blogProjectMain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # (r'^$', direct_to_template, {'template': 'base.html'}),
    # (r'^$', static_page, {'template': 'base'}),
    (r'^$', include('blog.urls')),
    (r'^(?P<template>\w+)/$', static_page),
)
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
        
    )