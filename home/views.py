from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from common.views import getSpecialStatuEvents

def homepageView(request):
    events = getSpecialStatuEvents(request,BEGIN_NOT_OVER)
    context = {
        "events":events,
    }
    return render(request,"home/homepage.html",context)