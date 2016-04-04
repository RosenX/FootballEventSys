#coding=utf-8
from const import *
from event.models import Event
from team.models import Team,Player,OtherMember
from datetime import date

def getEvents(request):
    event_list = Event.objects.all().order_by("-end_time")
    events =[]
    for event in event_list:
        if event.start_time > date.today(): events.append((event,NOT_BEGIN))
        elif event.end_time > date.today(): events.append((event,BEGIN_NOT_OVER))
        else: events.append((event,OVER))
    return events

def judgeStatu(request,event):
    if event.start_time > date.today(): return NOT_BEGIN
    elif event.end_time > date.today(): return BEGIN_NOT_OVER
    else: return OVER

def getSpecialStatuEvents(request,statu):
    event_list = Event.objects.all().order_by("-end_time")
    events=[]
    for event in event_list:
        s = judgeStatu(request, event)
        if statu == s: events.append(event)
    return events

def getTeams(request):
    team_list = Team.objects.all()
    return team_list

def getRoundsAndMathchs(request,event):
    rounds = event.schedule_set.all()
    rounds_matchs = []
    for r in rounds:
        rounds_matchs.append((r,r.singlematch_set.all()))
    return rounds_matchs
