#coding=utf-8
from const import TITLE_CHOICES
from django import  forms
from django.forms import ModelForm
from team.models import Team,Player,OtherMember

class TeamAddForm(ModelForm):
    class Meta:
        model=Team
        widgets={
            'team_name':forms.TextInput(attrs={'class':'form-control','label':"队名"}),
            'club':forms.TextInput(attrs={'class':'form-control',"lable":"俱乐部"}),
        }

class PlayerAddForm(ModelForm):
    class Meta:
        model = Player
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-control','label':"姓名"}),
            "team" : forms.HiddenInput(attrs={'class':'form-control team',"lable":"球队"}),
            "phone" : forms.TextInput(attrs={'class':'form-control',"lable":"电话"}),
            "email" : forms.TextInput(attrs={'class':'form-control',"lable":"电子邮件"}),
            "age" : forms.TextInput(attrs={'class':'form-control',"lable":"年龄"}),
            "number" : forms.TextInput(attrs={'class':'form-control',"lable":"号码"}),
        }

class MemberAddForm(ModelForm):
    class Meta:
        model = OtherMember
        widgets = {
            "name" : forms.TextInput(attrs={'class':'form-control','label':"姓名"}),
            "team" : forms.HiddenInput(attrs={'class':'form-control team',"lable":"球队"}),
            "phone" : forms.TextInput(attrs={'class':'form-control',"lable":"电话"}),
            "email" : forms.TextInput(attrs={'class':'form-control',"lable":"电子邮件"}),
            "age" : forms.TextInput(attrs={'class':'form-control',"lable":"年龄"}),
            "title" : forms.Select(attrs={'class':'form-control',"lable":"职位"}),
        }
    def __init__(self,*args,**kwargs):
        super(MemberAddForm,self).__init__(*args,**kwargs)
        self.fields["title"].choices = TITLE_CHOICES