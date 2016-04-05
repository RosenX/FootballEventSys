from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from notice import views as notice_views

urlpatterns = patterns('',
    url(
        r'^$',
        notice_views.noticeView
    ),
    url(
        r'^(?P<noticeId>\d+)$',
        notice_views.showNoticeView,
    )
)
