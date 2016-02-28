#coding=utf-8
from django import  forms
from django.forms import ModelForm
from event.models import Event,Schedule,SingleMatch
from team.models import Team

class EventAddForm(ModelForm):
    class Meta:
        model=Event
        widgets={
            'event_name':forms.TextInput(attrs={'class':'form-control','label':"比赛名称"}),
            'start_time':forms.TextInput(attrs={'class':'form-control datepicker','lable':"开始时间"}), 
            'end_time':forms.TextInput(attrs={'class':'form-control datepicker','lable':"结束时间"}),
            'place':forms.TextInput(attrs={'class':'form-control',"lable":"举办地点"}),
        }

class MatchAddForm(ModelForm):
    class Meta:
        model = SingleMatch
        exclude = ['teamA_score','teamB_score']
        widgets = {
            "teamA":forms.Select(attrs={'class':'form-control','label':"队1"}),
            "teamB":forms.Select(attrs={'class':'form-control','label':"队2"}),
            "date":forms.TextInput(attrs={'class':'form-control datepicker','label':"比赛时间"}),
            "round_belong":forms.HiddenInput(attrs={'class':'form-control','label':"第几轮"}),
            "referee":forms.TextInput(attrs={'class':'form-control','label':"裁判"}),
        }

    def __init__(self,*args,**kwargs):
        super(MatchAddForm,self).__init__(*args,**kwargs)
        teams = Team.objects.all()
        choices=tuple([(team.id,team.team_name) for team in teams])
        self.fields["teamA"].choices = choices
        self.fields["teamB"].choices = choices