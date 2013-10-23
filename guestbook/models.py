#coding=utf-8
from datetime import datetime
from django.db import models

class Msg(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    ip = models.IPAddressField(blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    add_date = models.DateTimeField(default=datetime.now)
    parent_id = models.IntegerField()

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = '留言'

    def __unicode__(self):
        return self.content


