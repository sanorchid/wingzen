# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db import models
from django.utils.translation import ugettext as _
from utils import datetime_to_timestamp


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('', _(u'一般事务')),
        ('event-warning', _(u'工作提醒')),
        ('event-info', _(u'工作信息')),
        ('event-success', _(u'工作捷报')),
        ('event-inverse', _(u'Inverse')),
        ('event-special', _(u'特殊事务')),
        ('event-important', _(u'重要情况')),
    )
    title = models.CharField(max_length=255, verbose_name=_(u'标题'))
    url = models.URLField(verbose_name=_(u'网址'))
    css_class = models.CharField(max_length=20, choices=CSS_CLASS_CHOICES, verbose_name=_(u'CSS类'))
    start = models.DateTimeField(verbose_name=_(u'开始日期'))
    end = models.DateTimeField(verbose_name=_(u'截止日期'), blank=True)

    @property
    def start_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.start)

    @property
    def end_timestamp(self):
        """
        Return end date as timestamp
        """
        return datetime_to_timestamp(self.end)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['end']
        verbose_name = u'日历事件'
        verbose_name_plural = u'日历事件'

