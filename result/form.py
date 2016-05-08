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

class RedCardAddForm(ModelForm):
    class Meta:
        model = RedCard
        widgets = {
            'player' : forms.Select(attrs={'class':'form-control','label':'球员'}),
            'match' : forms.HiddenInput(attrs={'class':'form-control','label':'比赛'}),
            'reason' : forms.Select(attrs={'class':'form-control','label':'原因'}),
            # player = models.ForeignKey(Player,verbose_name=u'球员',blank=False,null=False)
            # match = models.ForeignKey(SingleMatch,verbose_name=u"比赛",blank=False,null=False)
            # reason = models.CharField(verbose_name=u'原因',max_length=100,blank=True,null=True)
        }

class YellowCardAddForm(ModelForm):
    class Meta:
        model = YellowCard
        widgets = {
            'player' : forms.Select(attrs={'class':'form-control','label':'球员'}),
            'match' : forms.HiddenInput(attrs={'class':'form-control','label':'比赛'}),
            'reason' : forms.Select(attrs={'class':'form-control','label':'原因'}),
        }
