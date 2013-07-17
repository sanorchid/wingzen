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

GRADE_CHOICES = (
    (u'prs1', u'小学一年级'),
    (u'prs2', u'小学二年级'),
    (u'prs3', u'小学三年级'),
    (u'prs4', u'小学四年级'),
    (u'prs5', u'小学五年级'),
    (u'prs6', u'小学六年级'),
    (u'jns1', u'初中一年级'),
    (u'jns2', u'初中二年级'),
    (u'jns3', u'初中三年级'),
)

SUBJECT_CHOICES = (
    (u'chs', u'语文'),
    (u'eng', u'英语'),
    (u'mat', u'数学'),
    (u'sci', u'科学'),
)

TYPE_CHOICES = (
    (u'Cloze', u'完形填空'),
    (u'ReadingComprehension', u'阅读理解'),
)

class Choice(models.Model):
    answer = models.CharField(max_length=8, choices=ANSWER_CHOICES, verbose_name='答案')
    body = models.TextField()
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    class Meta:
        abstract = True

class ChoiceIndependent(Choice):
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name='年级')
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, verbose_name='科目')
    tags = TaggableManager(help_text = "标签之间请用逗号分隔")

class ChoiceDependent(Choice):
    bond = models.CharField(max_length=20)
    label = models.CharField(max_length=20)

class ChoiceMatch(models.Model):
    bond = models.CharField(max_length=20)
    choice1 = models.CharField(max_length=600)
    choice2 = models.CharField(max_length=600)
    choice3 = models.CharField(max_length=600)
    choice4 = models.CharField(max_length=600)
    choice5 = models.CharField(max_length=600)
    choice6 = models.CharField(max_length=600)
    label = models.CharField(max_length=20)

# Table 'Passage' deal with: 'cloze, readingcomprehension, 选词填空, etc.'
class Passage(models.Model):
    body = models.TextField()
    bond = models.CharField(max_length=20)
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name='年级')
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, verbose_name='科目')
    tags = TaggableManager(help_text = "标签之间请用逗号分隔")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='题目类型')

class PassageMatch(Passage):
    answer = models.CharField(max_length=8, choices=ANSWER_CHOICES, verbose_name='答案')

class Problem(models.Model):
    answer = models.CharField(max_length=200, verbose_name='答案')
    body = models.TextField()
    class Meta:
        abstract = True

class ProblemDependent(Problem):
    bond = models.CharField(max_length=20)
    label = models.CharField(max_length=20)

class ProblemIndependent(Problem):
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name='年级')
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, verbose_name='科目')
    tags = TaggableManager(help_text = "标签之间请用逗号分隔")

class BlankContext(models.Model):
    answer = models.CharField(max_length=200, verbose_name='答案')
    body = models.TextField()
    grade = models.CharField(max_length=20, choices=GRADE_CHOICES, verbose_name='年级')
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES, verbose_name='科目')
    tags = TaggableManager(help_text = "标签之间请用逗号分隔")

class FillContent(models.Model):
    answer = models.CharField(max_length=200, verbose_name='答案')
    bond = models.CharField(max_length=20)
    content = models.CharField(max_length=600)





