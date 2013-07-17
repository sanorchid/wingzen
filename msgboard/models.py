#coding=utf-8
from datetime import datetime
from django.db import models

class Msg(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    ip = models.IPAddressField(blank=True, null=True)
    add_date = models.DateTimeField(default=datetime.now)
    parent_id = models.IntegerField()
    def __unicode__(self):
        return self.content


