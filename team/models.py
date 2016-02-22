#coding=utf-8
from const import *
from django.db import models
# Create your models here.

class Team(models.Model):
	team_name = models.CharField(verbose_name=u'队名',max_length=50,blank=False,null=True)
	club = models.CharField(verbose_name=u'俱乐部',max_length=50)

	class Meta:
		verbose_name = u'球队'
		verbose_name_plural = u'球队'

	def __unicode__(self):
		return "%s"%self.team_name

# class Member(models.Model):
# 	name = models.CharField(verbose_name=u'姓名',max_length=50,blank=False,null=False)
# 	team = models.ForeignKey(Team,verbose_name=u'球队',blank=False,null=False)
# 	phone = models.CharField(verbose_name=u'电话',blank=True,null=True,max_length=30)
# 	email = models.EmailField(verbose_name=u'电子邮件',blank=True,null=True)
# 	age = models.IntegerField(verbose_name=u'年龄',blank=True,null=True)

# 	class Meta:
# 		verbose_name = u'成员'
# 		verbose_name_plural = u'成员'

# 	def __unicode__(self):
# 		return '%s'%self.name

class Player(models.Model):
	#player = models.OneToOneField(Member,blank=False,null=False)
	name = models.CharField(verbose_name=u'姓名',max_length=50,blank=False,null=False)
	team = models.ForeignKey(Team,verbose_name=u'球队',blank=False,null=False)
	phone = models.CharField(verbose_name=u'电话',blank=True,null=True,max_length=30)
	email = models.EmailField(verbose_name=u'电子邮件',blank=True,null=True)
	age = models.IntegerField(verbose_name=u'年龄',blank=True,null=True)
	number = models.IntegerField(verbose_name=u'号码',blank=True,null=True)

	class Meta:
		verbose_name = u'队员'
		verbose_name_plural = u'队员'

	def __unicode__(self):
		return '%s'%self.name

class OtherMember(models.Model):
	name = models.CharField(verbose_name=u'姓名',max_length=50,blank=False,null=False)
	team = models.ForeignKey(Team,verbose_name=u'球队',blank=False,null=False)
	phone = models.CharField(verbose_name=u'电话',blank=True,null=True,max_length=30)
	email = models.EmailField(verbose_name=u'电子邮件',blank=True,null=True)
	age = models.IntegerField(verbose_name=u'年龄',blank=True,null=True)
	#member = models.OneToOneField(Member,blank=False,null=False)
	title = models.IntegerField(choices=TITLE_CHOICES,verbose_name=u"职位",blank=True,null=True)

	class Meta:
		verbose_name = u'职员'
		verbose_name_plural = u'职员'

	def __unicode__(self):
		return "%s"%self.name