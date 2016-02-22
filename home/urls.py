from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from home import views as home_views

urlpatterns = patterns('',
    url(
        r'^$',
        home_views.homepageView
    ),
)

