#coding=utf-8
from django.db import models
from team.models import Team

class Event(models.Model):
	event_name = models.CharField(verbose_name=u'赛事名称',max_length=50,blank=False,null=False)
	start_time = models.DateField(verbose_name=u'开始时间',blank=False,null=False)
	end_time = models.DateField(verbose_name=u'结束时间',blank=False,null=False)
	place = models.CharField(verbose_name=u'举办地点',blank=False,null=False,max_length=50)

	class Meta:
		verbose_name = u'赛事'
		verbose_name_plural = u'赛事'

	def __unicode__(self):
		return "%s"%self.event_name

class Schedule(models.Model):
	event = models.ForeignKey(Event,verbose_name=u'赛事名称',blank=False,null=False)
	round_number = models.IntegerField(verbose_name=u"第几轮",blank=True,null=True)

	class Meta:
		verbose_name = u'轮'
		verbose_name_plural = u'轮'

	def __unicode__(self):
		return '%s第%s轮'%(self.event,self.round_number)

class SingleMatch(models.Model):
	teamA = models.ForeignKey(Team,verbose_name=u'A队',related_name='A_team')
	teamB = models.ForeignKey(Team,verbose_name=u'B队',related_name='B_team')
	date = models.DateField(verbose_name=u'日期',blank=False,null=False)
	round_belong = models.ForeignKey(Schedule,verbose_name=u'哪一轮',blank=False,null=False)
	referee = models.CharField(verbose_name=u'裁判',blank=True,null=True,max_length=30)
	teamA_score = models.IntegerField(verbose_name=u"A队得分",default=0,blank=True,null=False)
	teamB_score = models.IntegerField(verbose_name=u"B队得分",default=0,blank=True,null=False)

	class Meta:
		verbose_name = u'单场比赛'
		verbose_name_plural = u'单场比赛'
	def __unicode__(self):
		return "%s vs %s,%s"%(self.teamA,self.teamB,self.date)



