#coding = utf-8
from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from common.views import getSpecialStatuEvents,getRoundsAndMathchs, judgeStatu
from event.models import Event

def resultView(request):
    events = getSpecialStatuEvents(request,statu=BEGIN_NOT_OVER)
    context ={
        "event_list":events,
    }
    return render(request,"result/resulthome.html",context)

def resultEntryView(request,eventId):
    event = Event.objects.get(id=eventId)
    rounds_matchs = getRoundsAndMathchs(request,event)
    statu = judgeStatu(request,event)
    context ={
        "event":event,
        "rounds_matchs":rounds_matchs,
        "statu": statu,
    }
    return render(request,"result/result_entry.html",context)
