#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from wingoa.models import Staff, Inst, KlsWing, GENDER_CHOICES

# 成绩表，学习状态表考虑按年级分表
GRADE_CHOICES = (
    (u'grd01', u'一年'),
    (u'grd02', u'二年'),
    (u'grd03', u'三年'),
    (u'grd04', u'四年'),
    (u'grd05', u'五年'),
    (u'grd06', u'六年'),
    (u'grd07', u'七年'),
    (u'grd08', u'八年'),
    (u'grd09', u'九年'),
    (u'grd10', u'高一'),
    (u'grd11', u'高二'),
    (u'grd12', u'高三'),
    )

KLASS_CHOICES = (
    (u'kls01', u'一班'),
    (u'kls02', u'二班'),
    (u'kls03', u'三班'),
    (u'kls04', u'四班'),
    (u'kls05', u'五班'),
    (u'kls06', u'六班'),
    (u'kls07', u'七班'),
    (u'kls08', u'八班'),
    (u'kls09', u'九班'),
    (u'kls10', u'十班'),
    (u'kls11', u'十一班'),
    (u'kls12', u'十二班'),
    (u'kls13', u'十三班'),
    )

SUBJECT_CHOICES = (
    (u'allsubjects', u'全科'),
    (u'chinese', u'语文'),
    (u'math', u'数学'),
    (u'english', u'英语'),
    (u'science', u'科学'),
    (u'physics', u'物理'),
    (u'chemistry', u'化学'),
    (u'biology', u'生物'),
    (u'geography', u'地理'),
    )
#class Grade(models.Model):
#    name = models.CharField(max_length='20', verbose_name=u'所在年级')
#    class Meta:
#        verbose_name = u'年级'
#        verbose_name_plural = u'年级'

#    def __unicode__(self):
#        return self.name



class Csort(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'课程类别')
    class Meta:
        verbose_name = u'课程类别'
        verbose_name_plural = u'课程类别'
    def __unicode__(self):
        return self.name


#class Subject(models.Model):
 #   name = models.CharField(max_length='30', verbose_name=u'所属科目')
  #  class Meta:
   #     verbose_name = u'课程科目'
    #    verbose_name_plural = u'课程科目'
    #def __unicode__(self):
     #   return self.name

class Teacher(models.Model):
    staff = models.OneToOneField(Staff, verbose_name=u'教师姓名')
    name1 = models.CharField(max_length=10)
    grade = models.CharField(max_length=5, blank=True, null=True, choices=GRADE_CHOICES, verbose_name=u'所教年级')
    subject = models.CharField(max_length=15, blank=True, null=True, choices=SUBJECT_CHOICES, verbose_name=u'所教科目')
    is_teamleader = models.BooleanField(default=False, verbose_name=u'是否教学组长')

    class Meta:
        ordering = ['grade']
        verbose_name = u'教师'
        verbose_name_plural = u'教师'

    def __unicode__(self):
        return u'%s: %s%s, Tel:%s' % (self.staff.name, self.get_grade_display(), self.get_subject_display(), self.staff.telephone)

class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
    teachers = models.ManyToManyField(Teacher, verbose_name=u'授课教师')
    pub_date = models.DateTimeField(default = datetime.now)
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES, verbose_name=u'年级')
    klass = models.ForeignKey(KlsWing)
    subject = models.CharField(max_length=12, choices=SUBJECT_CHOICES, verbose_name=u'科目')
    inst = models.ForeignKey(Inst, verbose_name=u'所在校区')
    csort = models.ForeignKey(Csort)
    ctbgn_night = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课起始时间')
    ctend_night = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课结束时间')
    cd_night = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'上课日期')
    ctbgn_day = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课起始时间')
    ctend_day = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课结束时间')
    cd_day = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'上课日期')

    details = models.TextField(verbose_name=u'课程详情')
    is_recommended = models.BooleanField(default=False, verbose_name=u'是否推荐')

    class Meta:
        permissions = (
        ('view_course', 'can view courses'),
        )
        verbose_name = u'课程'
        verbose_name_plural = u'课程'
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.name

class CourseTuition(models.Model):
    course = models.ForeignKey(Course)
    tuition = models.CharField(max_length=100, verbose_name=u'授课费用')
    ctimes = models.CharField(max_length=20, verbose_name=u'授课次数')

    class Meta:
        verbose_name = u'课程费用'
        verbose_name_plural = u'课程费用'

    def __unicode__(self):
        return self.tuition

class Student(models.Model):
    STATUS_CHOICES = (
    (u'present', u'当前学员'),
    (u'trial', u'试读学员'),
    (u'graduate', u'毕业学员'),
    (u'dropout_on_trial', u'试读期退学学员'),
    (u'dropout_on_noeffect', u'效果不佳退学学员'),
    (u'dropout_on_others', u'其他原因退学学员'),
    )

    name = models.CharField(max_length=20, verbose_name=u'学生姓名')
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, default='M', verbose_name=u'学生性别')
    datentry = models.DateField(editable=True,verbose_name=u'入学日期')
    inst = models.ForeignKey(Inst, verbose_name=u'入学校区')
    course = models.ManyToManyField(Course, verbose_name=u'学习课程')
    school = models.CharField(max_length=60, verbose_name=u'所在学校')
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES, verbose_name=u'所在年级')
    klass = models.CharField(max_length=5, choices=KLASS_CHOICES, verbose_name=u'学校班级')
    telephone = models.CharField(max_length=20, verbose_name=u'联系电话')
    address = models.CharField(max_length=60, verbose_name=u'家庭住址')
    initchs = models.CharField(max_length=20, verbose_name=u'语文成绩')
    initmath = models.CharField(max_length=20, verbose_name=u'数学成绩')
    initeng = models.CharField(max_length=20, verbose_name=u'英语成绩')
    initsci = models.CharField(blank=True, null=True, max_length=20, verbose_name=u'科学成绩')
    initrnk = models.CharField(blank=True, null=True, max_length=20, verbose_name=u'年级排名')

    character = models.CharField(max_length=30, verbose_name=u'性格特点')
    csort = models.ForeignKey(Csort, verbose_name=u'授课形式')
    is_picked = models.BooleanField(verbose_name=u'是否接送')
    is_dining = models.BooleanField(default=True, verbose_name=u'是否在校就餐')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name=u'学员状态',default=u'trial')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name=u'备注')
    receiver = models.CharField(max_length=6, default=u'周显迪', verbose_name=u'接收人')
    class Meta:
        permissions=(
        ('view_student', 'can view students'),
        )
        verbose_name = u'学生'
        verbose_name_plural = u'学生'
        ordering = ['name']

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






#class StuCourse(models.Model):
 #   student = models.ForeignKey(Student)
  #  course = models.ManyToManyField(Course)
   # class Meta:
    #    verbose_name = u'学生所学课程'
     #   verbose_name_plural = u'学生所学课程'
    #def __unicode__(self):
     #   return self.student

class StuTuition(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学生')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    datefrom= models.DateField(editable=True, verbose_name=u'开始日期')
    dateto = models.DateField(editable=True, verbose_name=u'结束日期')
    tuition = models.CharField(max_length=30, verbose_name=u'学费')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name=u'备注')

    class Meta:
        verbose_name = u'学生学费'
        verbose_name_plural = u'学生学费'
        ordering = ['dateto']
    def __unicode__(self):
        return u'%s: %s' % (self.student, self.tuition)


class SchExam(models.Model):
    name = models.CharField(max_length=80, verbose_name=u'考试名称')
    date = models.DateField(editable=True, verbose_name=u'考试日期')
    region = models.CharField(max_length=20, verbose_name=u'覆盖范围')
    subject = models.CharField(max_length=12, choices=SUBJECT_CHOICES, verbose_name=u'科目')

    class Meta:
        verbose_name = u'学校考试'
        verbose_name_plural = u'学校考试'
    def __unicode__(self):
        return u'%s--%s' % (self.date, self.name)

class Score(models.Model):
    student = models.ForeignKey(Student, verbose_name=u'学生')
    exam = models.ForeignKey(SchExam, verbose_name=u'考试')
    english = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'英语成绩')
    chinese = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'语文成绩')
    maths = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'数学成绩')
    science = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'科学成绩')
    physics = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'物理成绩')
    chemistry = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'化学成绩')
    biology = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=u'生物成绩')
    rank = models.CharField(max_length=50, verbose_name=u'排名')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name=u'备注')

    class Meta:

        verbose_name = u'考试成绩'
        verbose_name_plural = u'考试成绩'
        ordering = ['exam']
    def __unicode__(self):
        return u'%s: %s' % (self.student, self.exam)



class StuRecord(models.Model):
    student = models.ForeignKey(Student)
    datefrom = models.DateField(editable=True, verbose_name=u'开始日期')
    dateto = models.DateField(editable=True, verbose_name=u'结束日期')
    stustat = models.CharField(max_length=250, verbose_name=u'学习状态')
    stugoal = models.CharField(max_length=250, verbose_name=u'学习目标')
    is_focus = models.BooleanField(default=False, verbose_name=u'是否重点关注')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name=u'备注')

    class Meta:
        verbose_name = u'学习记录'
        verbose_name_plural = u'学习记录'
        ordering = ['student']
    def __unicode__(self):
        return u'%s (%s-%s) : %s-%s' % (self.student, self.datefrom, self.dateto, self.stustat, self.stugoal)





