from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from common.views import getSpecialStatuEvents
from notice.models import Notice

def homepageView(request):
    events_ing = getSpecialStatuEvents(request, BEGIN_NOT_OVER)
    events_over = getSpecialStatuEvents(request, OVER)
    notice_list = Notice.objects.all()
    context = {
        "events": events_ing + events_over,
        "notice_list": notice_list, 
    }
    return render(request,"home/homepage.html",context)
