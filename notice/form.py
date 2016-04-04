#coding=utf-8
from django import  forms
from django.forms import ModelForm
from notice.models import Notice

class NoticeAddForm(ModelForm):
    class Meta:
        model = Notice
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','label':"标题"}),
            'content':forms.Textarea(attrs={'class':'form-control','lable':"正文"}),
        }
