from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.template.loader import render_to_string
from django.utils import simplejson
from event.models import SingleMatch
from result.models import Score,RedCard,YellowCard
from common.views import getTeams
from result.form import ScoreAddForm,RedCardAddForm,YellowCardAddForm

def getScores(request,match):
    A_score = Score.objects.filter(match=match,player__team=match.teamA);
    A_score = [score for score in A_score]
    B_score = Score.objects.filter(match=match,player__team=match.teamB);
    B_score = [score for score in B_score]
    tmp = [Score()]*abs(len(A_score)-len(B_score))
    if len(A_score) > len(B_score):B_score.append(tmp)
    if len(A_score) < len(B_score):A_score.append(tmp)
    scores = [(A_score[i],B_score[i]) for i in range(len(A_score))]
    return scores

@dajaxice_register
def getCards(request,matchId):
    match = SingleMatch.objects.get(id=matchId)
    match_cards_table = generateCardRecordHmtl(match)
    context = {
        'html' : match_cards_table,
    }
    return simplejson.dumps(context)

@dajaxice_register
def getMatch(request,matchId):
    match = SingleMatch.objects.get(id=matchId)
    scores = getScores(request,match)
    form = ScoreAddForm()
    match_score_table = render_to_string("result/widget/score_record.html",{
        "match":match,
        "scores":scores,
        "form":form,
    })
    context={
        "html":match_score_table,
    }
    return simplejson.dumps(context)

@dajaxice_register
def addScore(request,form,matchId,which_team):
    form = ScoreAddForm(deserialize_form(form))
    context={}
    if form.is_valid():
        form.save()
        number = int(form.cleaned_data["number"])
        match = SingleMatch.objects.get(id=matchId)
        if which_team == 'A':match.teamA_score += number
        if which_team == 'B':match.teamB_score += number
        match.save()
        scores = getScores(request,match)
        form = ScoreAddForm()
        match_score_table = render_to_string("result/widget/score_record.html",{
            "match":match,
            "scores":scores,
            "form":form,
        })
        context["statu"] = SUCCESS
        context["html"] = match_score_table
    else:
        print form
        #print form.errors
        context["statu"] = ERROR
    return simplejson.dumps(context)

def generateCardRecordHmtl(match):
    red_card_list = RedCard.objects.filter(match = match)
    yellow_card_list = YellowCard.objects.filter(match = match)
    red_form = RedCardAddForm()
    yellow_form = YellowCardAddForm()
    context = {
        'match' : match,
        'red_card_list' : red_card_list,
        'yellow_card_list' : yellow_card_list,
        'red_form' : red_form,
        'yellow_form' : yellow_form,
    }
    return render_to_string("result/widget/card_record.html",context)

@dajaxice_register
def addRedCard(request,form):
    form = RedCardAddForm(deserialize_form(form))
    context = {}
    if form.is_valid():
        form.save()
        match = form.cleaned_data["match"]
        match_cards_table = generateCardRecordHmtl(match)
        context = {
            'html' : match_cards_table,
        }
        context["statu"] = SUCCESS
    else:
        context["statu"] = ERROR
    return simplejson.dumps(context)

@dajaxice_register
def addYellowCard(request,form):
    form = YellowCardAddForm(deserialize_form(form))
    context = {}
    if form.is_valid():
        form.save()
        match = form.cleaned_data["match"]
        match_cards_table = generateCardRecordHmtl(match)
        context = {
            'html' : match_cards_table,
        }
        context["statu"] = SUCCESS
    else:
        context["statu"] = ERROR
    return simplejson.dumps(context)
