from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from team.form import TeamAddForm,PlayerAddForm,MemberAddForm
from team.models import Team
from django.template.loader import render_to_string
from django.utils import simplejson
from common.views import getTeams

@dajaxice_register
def addTeam(request,form):
    form = TeamAddForm(deserialize_form(form))
    context={}
    if form.is_valid():
        form.save()
        teams = getTeams(request)
        team_list_table = render_to_string("team/widget/team_list.html",{"team_list":teams})
        context["html"]= team_list_table
        context["statu"]=SUCCESS 
    else: 
        context["statu"]=ERROR
    return simplejson.dumps(context)

@dajaxice_register
def addPlayer(request,form,teamId):
    form = PlayerAddForm(deserialize_form(form))
    context={}
    if form.is_valid():
        form.save()
        team = Team.objects.get(id=teamId)
        play_list = team.player_set.all()
        play_list_table = render_to_string("team/widget/player_list.html",{"team":team,"player_list":play_list})
        context["statu"]=SUCCESS
        context["html"]=play_list_table
    else:
        context["statu"]=ERROR
    return simplejson.dumps(context)

@dajaxice_register
def addMember(request,form,teamId):
    form = MemberAddForm(deserialize_form(form))
    context={}
    if form.is_valid():
        print "hello"
        form.save()
        team = Team.objects.get(id=teamId)
        member_list = team.othermember_set.all()
        member_list_table = render_to_string("team/widget/member_list.html",{"team":team,"member_list":member_list})
        context["statu"]=SUCCESS
        context["html"]=member_list_table
    else:
        print form.errors
        context["statu"]=ERROR
    return simplejson.dumps(context)

