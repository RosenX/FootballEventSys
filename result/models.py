#coding=utf-8
from django.db import models
from team.models import Team,Player
from event.models import SingleMatch,Event

class Score(models.Model):
    player = models.ForeignKey(Player,verbose_name=u'球员',blank=False,null=False)
    match =models.ForeignKey(SingleMatch,verbose_name=u'比赛',blank=False,null=False)
    number = models.IntegerField(verbose_name=u'个数',blank=False,null=False)

    class Meta:
        verbose_name = u'进球'
        verbose_name_plural = u'进球'

    def __unicode__(self):
        return u"%s(%s)"%(self.player,self.match)

class RedCard(models.Model):
    player = models.ForeignKey(Player,verbose_name=u'球员',blank=False,null=False)
    match = models.ForeignKey(SingleMatch,verbose_name=u"比赛",blank=False,null=False)
    reason = models.CharField(verbose_name=u'原因',max_length=100,blank=True,null=True)

    class Meta:
        verbose_name = u'红牌'
        verbose_name_plural = u'红牌'

    def __unicode__(self):
        return u"%s(%s)"%(self.player,self.match)

class YellowCard(models.Model):
    player = models.ForeignKey(Player,verbose_name=u'球员',blank=False,null=False)
    match = models.ForeignKey(SingleMatch,verbose_name=u"比赛",blank=False,null=False)
    reason = models.CharField(verbose_name=u'原因',max_length=100,blank=True,null=True)

    class Meta:
        verbose_name = u'黄牌'
        verbose_name_plural = u'黄牌'

    def __unicode__(self):
        return u"%s(%s)"%(self.player,self.match)

class SumScore(models.Model):
    team = models.ForeignKey(Team,verbose_name=u'球队',blank=False,null=False)
    event = models.ForeignKey(Event,verbose_name=u'赛事',blank=False,null=False)
    sum_score = models.IntegerField(default=0,blank=False,null=False,verbose_name=u'积分')

    class Meta:
        verbose_name = u'积分'
        verbose_name_plural = u'积分'

    def __unicode__(self):
        return u"%s(%s):%d"%(self.team.team_name,self.event.event_name,self.sum_score)
