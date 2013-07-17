#coding=utf-8

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from django.conf import settings

class TagsUsed(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True)

ANSWER_CHOICES = (
    (u'A', u'A'),
    (u'B', u'B'),
    (u'C', u'C'),
    (u'D', u'D'),
    (u'E', u'E'),
    (u'F', u'F'),
)

class Question(models.Model):
    tags = TaggableManager(help_text = "标签之间请用逗号分隔")
    answer = models.CharField(max_length=8, choices=ANSWER_CHOICES, verbose_name='答案')
    qid = models.CharField(max_length=6, verbose_name='序号')
    class Meta:
        abstract = True

class Qindp(Question):
    body = models.CharField(max_length=500)    
    class Meta:
        abstract = True

class Choice3(models.Model):
    choiceA = models.CharField(max_length=250)
    choiceB = models.CharField(max_length=250)
    choiceC = models.CharField(max_length=250)
    def __unicode__(self):
        return u'A:%s, B:%s, C:%s' % (self.choiceA, self.choiceB, self.choiceC)

class Choice4(Choice3):
    choiceD = models.CharField(max_length=250)
    def __unicode__(self):
        return u'A:%s, B:%s, C:%s, D:%s' % (self.choiceA, self.choiceB, self.choiceC, self.choiceD)

class Choice6(Choice4):
    choiceE = models.CharField(max_length=250)
    choiceF = models.CharField(max_length=250)
    ckey = models.CharField(max_length=25, unique=True, help_text="此标记不能重复。")
    def __unicode__(self):
        return u'%s' % (self.ckey)

class Passage(models.Model):
    body = models.TextField()
    slug = models.SlugField(unique = True, help_text = "短文标记根据内容自动生成，请保证该字段唯一。")
    def __unicode__(self):
        return u'%s: %s' % (self.grade, self.slug)

# English Choices Tables. 
# 英语单选题
class EngSglChoice(Qindp):
    choice = models.ForeignKey(Choice4)

# 完形填空
class EngClzChoice(Question):
    choice = models.ForeignKey(Choice4)
    passage = models.ForeignKey(Passage)

# 阅读理解1
class EngRdhChoice1(Qindp):
    choice = models.ForeignKey(Choice4)
    passage = models.ForeignKey(Passage)

# 阅读理解2
class EngRdhChoice2(Qindp):
    choice = models.ForeignKey(Choice6)


# u'题目有相应图表的也加上'








