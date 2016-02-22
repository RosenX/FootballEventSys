from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from event import views as event_views

urlpatterns = patterns('',
    url(
        r'^$',
        event_views.eventView
    ),
    url(
        r'^(?P<eventId>\d+)$',
        event_views.arrangeScheduleView
    )
)

