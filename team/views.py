from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from team.models import Team,Player,OtherMember
from common.views import getTeams
from team.form import TeamAddForm,PlayerAddForm,MemberAddForm
from datetime import date


def teamView(request):
    teams = getTeams(request)
    form = TeamAddForm()
    context={
        'form':form,
        "team_list":teams
    }
    return render(request,"team/teamhome.html",context)

def teamManageView(request,teamId):
    form = PlayerAddForm()
    member_form = MemberAddForm()
    team = Team.objects.get(id=teamId)
    play_list = team.player_set.all()
    member_list = team.othermember_set.all()
    context={
        "form":form,
        "member_form":member_form,
        "team":team,
        "player_list":play_list,
        "member_list":member_list,
    }
    return render(request,"team/team_manage.html",context)
