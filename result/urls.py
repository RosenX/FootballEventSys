from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from result import views as result_views

urlpatterns = patterns('',
    url(
        r'^$',
        result_views.resultView
    ),
    url(
        r'^(?P<eventId>\d+)$',
        result_views.resultEntryView
    ),
)

