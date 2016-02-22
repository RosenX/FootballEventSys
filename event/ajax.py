from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from event.form import EventAddForm,MatchAddForm
from event.models import Event,Schedule,SingleMatch
from django.template.loader import render_to_string
from django.utils import simplejson
from common.views import getEvents,getRoundsAndMathchs

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
    event = Event.objects.get(id=event_id)
    new_round = Schedule(event=event)
    context={}
    try:
        new_round.save()
        rounds_matchs = getRoundsAndMathchs(request,event)
        rounds_matchs_table = render_to_string("event/widget/rounds_matchs_table.html",{"rounds_matchs":rounds_matchs})
        context["statu"]=SUCCESS
        context["html"]=rounds_matchs_table
    except Exception,e:
        context["statu"]=ERROR
    return simplejson.dumps(context)

@dajaxice_register
def addNewMatch(request,form,event_id):
    form = MatchAddForm(deserialize_form(form))
    event = Event.objects.get(id=event_id)
    context={}
    print "hello"
    if form.is_valid():
        form.save()
        new_form =MatchAddForm()
        rounds_matchs = getRoundsAndMathchs(request,event)
        rounds_matchs_table = render_to_string("event/widget/rounds_matchs_table.html",
                                                {"rounds_matchs":rounds_matchs,'form':form})
        context["statu"]=SUCCESS
        context["html"]=rounds_matchs_table
    else: 
        context["statu"]=ERROR
    return simplejson.dumps(context)

