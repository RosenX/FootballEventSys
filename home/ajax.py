from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from event.form import EventAddForm,MatchAddForm
from event.models import Event,Schedule,SingleMatch
from result.models import SumScore
from django.template.loader import render_to_string
from django.utils import simplejson
from common.views import getEvents,getRoundsAndMathchs,judgeStatu

@dajaxice_register
def getRank(request,event_id):
    event = Event.objects.get(id = event_id)
    context = {}
    sumscore_rank = SumScore.objects.filter(event = event).order_by("-sum_score")
    rounds_matchs = getRoundsAndMathchs(request, event)

    sumscore_rank_html = render_to_string('home/widgets/score_rank.html',{'sumscore_rank': sumscore_rank})
    rounds_matchs_html = render_to_string('home/widgets/round_score.html',{'rounds_matchs': rounds_matchs})
    context['sumscore_rank_html'] = sumscore_rank_html
    context['rounds_matchs_html'] = rounds_matchs_html

    return simplejson.dumps(context)
