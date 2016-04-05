#coding=utf-8
from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from event.form import EventAddForm,MatchAddForm
from event.models import Event,Schedule,SingleMatch
from team.models import Player
from result.models import SumScore
from django.template.loader import render_to_string
from django.utils import simplejson
from common.views import getEvents,getRoundsAndMathchs,judgeStatu

@dajaxice_register
def getRank(request,event_id):
    event = Event.objects.get(id = event_id)
    context = {}

    #获取球员排行榜
    rounds = event.schedule_set.all()
    rounds_matchs = []
    matchs = []
    match_scores = []
    scores = []
    for r in rounds: rounds_matchs.append(r.singlematch_set.all())
    for ms in rounds_matchs:
        for s in ms: matchs.append(s)
    for match in matchs: match_scores.append(match.score_set.all())
    for ms in match_scores:
        for s in ms: scores.append(s)
    player_stat = {}
    for score in scores:
        if score.player not in player_stat: player_stat[score.player] = 0
        player_stat[score.player] += score.number
    player_list = [(key, player_stat[key]) for key in player_stat]
    player_list.sort(key = lambda x: x[1], reverse = True)

    player_rank_html = render_to_string('home/widgets/top_scorer.html', {'player_rank_list':player_list})
    context['player_rank_html'] = player_rank_html

    #获取每轮成绩
    rounds_matchs = getRoundsAndMathchs(request, event)
    rounds_matchs_html = render_to_string('home/widgets/round_score.html',{'rounds_matchs': rounds_matchs})
    context['rounds_matchs_html'] = rounds_matchs_html

    #获取积分榜
    team_stat = {}
    for match in matchs:
        if match.teamA not in team_stat: team_stat[match.teamA] = 0
        if match.teamB not in team_stat: team_stat[match.teamB] = 0
        if match.teamA_score > match.teamB_score: team_stat[match.teamA] += WIN_SCORE
        if match.teamA_score == match.teamB_score:
            team_stat[match.teamA] += TAIL_SCORE
            team_stat[match.teamB] += TAIL_SCORE
        if match.teamA_score < match.teamB_score: team_stat[match.teamB] += WIN_SCORE

    team_rank_list = [(key, team_stat[key]) for key in team_stat]
    team_rank_list.sort(key = lambda x: x[1], reverse = True)

    sumscore_rank_html = render_to_string('home/widgets/score_rank.html',{'sumscore_rank': team_rank_list})
    context['sumscore_rank_html'] = sumscore_rank_html



    return simplejson.dumps(context)
