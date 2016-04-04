#coding=utf-8
from django.db import models


class Notice(models.Model):
    title = models.CharField(verbose_name = u'标题', max_length = 200, blank = False, null = False)
    content = models.CharField(verbose_name = u'内容', max_length =1000, blank = False, null = False)
    date = models.DateField(verbose_name = u'日期', auto_now_add = True)

    class Meta:
        verbose_name = u'通知'
        verbose_name_plural = u'通知'

    def __unicode__(self):
        return u'%s'%self.title
