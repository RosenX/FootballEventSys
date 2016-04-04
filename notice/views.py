#coding = utf-8
from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from common.views import getSpecialStatuEvents,getRoundsAndMathchs
from notice.models import Notice
from notice.form import NoticeAddForm

def noticeView(request):
    notice_list = Notice.objects.all()
    form = NoticeAddForm()
    context = {
        'notice_list':notice_list,
        'form':form,
    }
    return render(request,"notice/notice_home.html",context)
