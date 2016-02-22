#coding=utf-8
from django import  forms
from django.forms import ModelForm
from result.models import Score,RedCard,YellowCard
from team.models import Team

class ScoreAddForm(ModelForm):
    class Meta:
        model=Score
        widgets={
            'player':forms.Select(attrs={'class':'form-control','label':"球员"}),
            'match':forms.HiddenInput(attrs={'class':'form-control datepicker','lable':"比赛"}), 
            'number':forms.TextInput(attrs={'class':'form-control datepicker','lable':"进球数"}),
        }
