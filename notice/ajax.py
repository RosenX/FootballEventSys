from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.template.loader import render_to_string
from django.utils import simplejson
from common.views import getEvents,getRoundsAndMathchs,judgeStatu
from notice.form import NoticeAddForm
from notice.models import Notice
from const import *

@dajaxice_register
def addNotice(request,form):
    form = NoticeAddForm(deserialize_form(form))
    context={}
    if form.is_valid():
        form.save()
        notice = Notice.objects.all()
        notice_list_table = render_to_string("notice/widget/notice_list.html",{"notice_list":notice})
        context["html"] = notice_list_table
        context["statu"] = SUCCESS
    else:
        context["statu"] = ERROR
    return simplejson.dumps(context)

@dajaxice_register
def deleteNotice(request, notice_id):
    notice = Notice.objects.get(id = notice_id)
    context = {}
    try:
        notice.delete()
        notice = Notice.objects.all()
        notice_list_table = render_to_string("notice/widget/notice_list.html",{"notice_list":notice})
        context['html'] = notice_list_table
        context['statu'] = SUCCESS
    except:
        context['statu'] = ERROR
    return simplejson.dumps(context)
