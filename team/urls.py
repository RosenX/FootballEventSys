from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from team import views as team_views

urlpatterns = patterns('',
    url(
        r'^$',
        team_views.teamView
    ),
    url(
        r'^(?P<teamId>\d+)$',
        team_views.teamManageView
    ),
)