#coding=utf-8
from datetime import datetime
from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length='20', verbose_name=u'所在年级')

    def __unicode__(self):
        return self.name

class Student(models.Model):
    GENDER_CHOICES = (
        (u'M', u'男'),
        (u'F', u'女'),
    )
    GRADE_CHOICES = (
        (u'prs6', u'小学六年级'),
        (u'jns1', u'初中一年级'),
        (u'jns2', u'初中二年级'),
        (u'jns3', u'初中三年级'),
    )
    STATUS_CHOICES = (
        (u'on', u'当前学员'),
        (u'off', u'往期学员'),
    )
    name = models.CharField(max_length=20, verbose_name='学生姓名')
    spell = models.CharField(max_length=20, verbose_name='姓名拼音')
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='学生性别')
    grade = models.ForeignKey(Grade)
    klass = models.CharField(max_length=30, verbose_name='所在班级')
    school = models.CharField(max_length=60, verbose_name='所在学校')
    telephone = models.CharField(max_length=20, verbose_name='联系电话')
    address = models.CharField(max_length=60, verbose_name='家庭住址')
    class Meta:
        ordering = ['spell']
    
    def __unicode__(self):
        return self.name
    
    # "upgrade" do not function. Need to figure out another solution.
    #def save(self, *args, **kargs):
     #   if datetime.now().month == 9 and datetime.now().day == 1 and status =='off':
      #      if grade == 'prs6':
       #         self.grade = 'jns1'
        #    elif grade == 'jns1':
         #       self.grade = 'jns2'
          #  elif grade == 'jns2':
           #     self.grade = 'jns3'
        #super(Student, self).save(*args, **kargs)


class Score(models.Model):
    student = models.ForeignKey(Student)
    tname = models.CharField(max_length=80, verbose_name='考试名称')
    tdate = models.DateField(editable=True, verbose_name='考试日期')
    english = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='英语成绩')
    chinese = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='语文成绩')
    maths = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='数学成绩')
    science = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='科学成绩')
    physics = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='物理成绩')
    chemistry = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='化学成绩')
    biology = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='生物成绩')
    rank = models.CharField(max_length=50, verbose_name='排名')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name='备注')

    class Meta:
        ordering = ['tname']
    def __unicode__(self):
        return u'%s: %s' % (self.student, self.tname)
    
class Tuition(models.Model):
    student = models.ForeignKey(Student)
    tuition = models.CharField(max_length=30, verbose_name='学费')
    datefrom= models.DateField(editable=True, verbose_name='开始日期')
    dateto = models.DateField(editable=True, verbose_name='结束日期')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name='备注')


    class Meta:
        ordering = ['dateto']
    def __unicode__(self):
        return u'%s: %s' % (self.student, self.tuition)
 
 
class Sturec(models.Model):
    student = models.ForeignKey(Student)
    datefrom = models.DateField(editable=True, verbose_name='开始日期')
    dateto = models.DateField(editable=True, verbose_name='结束日期')
    stustat = models.CharField(max_length=250, verbose_name='学习状态')
    stugoal = models.CharField(max_length=250, verbose_name='学习目标')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name='备注')

    class Meta:
        ordering = ['student']
    def __unicode__(self):
        return u'%s (%s-%s) : %s-%s' % (self.student, self.datefrom, self.dateto, self.stustat, self.stugoal)

class Staff(models.Model):
    GENDER_CHOICES = (
        (u'M', u'男'),
        (u'F', u'女'),
    )    

    name = models.CharField(max_length=10, verbose_name='职工姓名')
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, default='F', verbose_name='性别')
    sid = models.CharField(max_length=20, verbose_name='身份证号')
    grade = models.CharField(max_length=10, verbose_name='文化程度')
    graduate = models.CharField(max_length=40, verbose_name='毕业学校')
    major = models.CharField(max_length=20, verbose_name='所学专业')
    datentry = models.DateField(editable=True,verbose_name='入职日期')
    department = models.CharField(max_length=20, verbose_name='所属部门')
    position = models.CharField(max_length=10, verbose_name='所属职位')
    rank = models.CharField(max_length=10, verbose_name='所属级别')
    telephone = models.CharField(max_length=20, verbose_name='联系电话')

    class Meta:
        ordering = ['datentry']
    def __unicode__(self):
        return u'%s: %s, %s, %s' % (self.name, self.datentry, self.position, self.rank)
            



    
        