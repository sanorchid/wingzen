#coding=utf-8
from django.db import models
from datetime import datetime
from eduzen.models import Grade 

class Csort(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'课程类别')

    def __unicode__(self):
        return self.name



class Cinst(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'所属机构')
 
    def __unicode__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'所属科目')

    def __unicode__(self):
        return self.name


   
class Course(models.Model):
    CSORT_CHOICES = (
        (u'tbxb', u'同步小班'),
        (u'zmxb', u'周末小班'),
        (u'sjtg', u'暑假提高班'),
        (u'xscgd', u'小升初过渡班'),
        (u'ydyjf', u'一对一精辅'),
    )
    CINST_CHOICES = (
        (u'gcq', u'拱宸桥校区'),
        (u'dsq', u'打索桥校区'),
    )
    GRADE_CHOICES = (
        (u'prs4', u'小学四年级'),
        (u'prs5', u'小学五年级'),
        (u'prs6', u'小学六年级'),
        (u'jns1', u'初中一年级'),
        (u'jns2', u'初中二年级'),
        (u'jns3', u'初中三年级'),
    )
    SUBJECT_CHOICES = (
        (u'chinese', u'语文'),
        (u'maths', u'数学'),
        (u'english', u'英语'),
        (u'science', u'科学'),
        (u'physics', u'物理'),
        (u'chemistry', u'化学'),
        (u'biology', u'生物'),
        (u'allsbj', u'全科'),
    )

    name = models.CharField(max_length=50, verbose_name='课程名称')
    pub_date = models.DateTimeField(default = datetime.now)
    grade = models.ForeignKey(Grade)
    subject = models.ForeignKey(Subject)
    cinst = models.ForeignKey(Cinst)
    csort = models.ForeignKey(Csort)
    cdate = models.CharField(max_length=50, verbose_name='授课时间')
    ctimes = models.CharField(max_length=20, verbose_name='授课次数')
    tuition = models.CharField(max_length=20, verbose_name='授课费用')
    details = models.TextField(verbose_name='课程详情')
    recommend = models.BooleanField(default=False, verbose_name='是否推荐')

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.name




