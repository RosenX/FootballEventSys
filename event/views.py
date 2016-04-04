from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from event.models import Event
from event.form import EventAddForm,MatchAddForm
from common.views import getEvents,getRoundsAndMathchs,judgeStatu
from datetime import date

def eventView(request):
    events = getEvents(request)
    form = EventAddForm()
    context={
        "form":form,
        "event_list":events,
    }
    return render(request,"event/eventhome.html",context)

def checkResultView(request, eventId):
    return ""

def arrangeScheduleView(request, eventId):
    event = Event.objects.get(id=eventId)
    statu = judgeStatu(request,event)
    rounds_matchs = getRoundsAndMathchs(request,event)
    form = MatchAddForm()
    context ={
        "event":event,
        "form":form,
        "rounds_matchs":rounds_matchs,
        "statu":statu,
    }
    return render(request,"event/event_schedule.html",context)
