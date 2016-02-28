from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from event.form import EventAddForm,MatchAddForm
from event.models import Event,Schedule,SingleMatch
from django.template.loader import render_to_string
from django.utils import simplejson
from common.views import getEvents,getRoundsAndMathchs,judgeStatu

@dajaxice_register
def addEvent(request,form):
    form = EventAddForm(deserialize_form(form))
    context={}
    if form.is_valid():
        form.save()
        events = getEvents(request)
        event_list_table = render_to_string("event/widget/event_list.html",{"event_list":events})
        context["html"]= event_list_table
        context["statu"]=SUCCESS 
    else: 
        context["statu"]=ERROR
    return simplejson.dumps(context)

@dajaxice_register
def addNewRound(request,event_id):
    form =MatchAddForm()
    event = Event.objects.get(id=event_id)
    new_round = Schedule(event=event)
    statu = judgeStatu(request,event)
    context={}
    try:
        new_round.save()
        rounds_matchs = getRoundsAndMathchs(request,event)
        rounds_matchs_table = render_to_string("event/widget/rounds_matchs_table.html",
                                                {"rounds_matchs":rounds_matchs,"statu":statu,'form':form})
        context["statu"]=SUCCESS
        context["html"]=rounds_matchs_table
    except Exception,e:
        print e
        context["statu"]=ERROR
    return simplejson.dumps(context)

@dajaxice_register
def addNewMatch(request,form,event_id):
    form = MatchAddForm(deserialize_form(form))
    event = Event.objects.get(id=event_id)
    statu = judgeStatu(request,event)
    context={}
    print "hello11"
    if form.is_valid():
        form.save()
        new_form =MatchAddForm()
        rounds_matchs = getRoundsAndMathchs(request,event)
        rounds_matchs_table = render_to_string("event/widget/rounds_matchs_table.html",
                                                {"rounds_matchs":rounds_matchs,'form':form,"statu":statu})
        context["statu"]=SUCCESS
        context["html"]=rounds_matchs_table
    else: 
        print form.errors
        context["statu"]=ERROR
    return simplejson.dumps(context)

