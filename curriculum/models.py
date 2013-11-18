#coding=utf-8
from datetime import datetime
from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length='20', verbose_name=u'所在年级')
    class Meta:
        verbose_name = u'年级'
        verbose_name_plural = u'年级'

    def __unicode__(self):
        return self.name

class KlassWiz(models.Model):
    name = models.CharField(max_length='20', verbose_name=u'文臻班级')
    class Meta:
        verbose_name = u'文臻班级'
        verbose_name_plural = u'文臻班级'

    def __unicode__(self):
        return self.name

class Csort(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'课程类别')
    class Meta:
        verbose_name = u'课程类别'
        verbose_name_plural = u'课程类别'
    def __unicode__(self):
        return self.name

class Cinst(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'所属机构')
    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = u'课程机构'

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'所属科目')
    class Meta:
        verbose_name = u'课程科目'
        verbose_name_plural = u'课程科目'
    def __unicode__(self):
        return self.name

class Student(models.Model):
    GENDER_CHOICES = (
        (u'M', u'男'),
        (u'F', u'女'),
    )

    STATUS_CHOICES = (
        (u'on', u'当前学员'),
        (u'off', u'往期学员'),
    )
    name = models.CharField(max_length=20, verbose_name=u'学生姓名')
    spell = models.CharField(max_length=20, verbose_name=u'姓名拼音')
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name=u'学生性别')
    grade = models.ForeignKey(Grade,verbose_name=u'所在年级')
    klass = models.CharField(max_length=30, verbose_name=u'学校班级')
    school = models.CharField(max_length=60, verbose_name=u'所在学校')
    telephone = models.CharField(max_length=20, verbose_name=u'联系电话')
    address = models.CharField(max_length=60, verbose_name=u'家庭住址')
    class Meta:
        verbose_name = u'学生'
        verbose_name_plural = u'学生'
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

class Teacher(models.Model):
    GENDER_CHOICES = (
        (u'M', u'男'),
        (u'F', u'女'),
    )

    name = models.CharField(max_length=10, verbose_name=u'教师姓名')
    sex = models.CharField(max_length=2, choices=GENDER_CHOICES, default='F', verbose_name=u'性别')
    sid = models.CharField(max_length=20, verbose_name=u'身份证号')
    graduate = models.CharField(max_length=40, verbose_name=u'毕业学校')
    major = models.CharField(max_length=20, verbose_name=u'所学专业')
    datentry = models.DateField(editable=True,verbose_name=u'入职日期')
    department = models.CharField(max_length=20, verbose_name=u'所属部门')
    position = models.CharField(max_length=10, verbose_name=u'所属职位')
    rank = models.CharField(max_length=10, verbose_name=u'所属级别')
    telephone = models.CharField(max_length=20, verbose_name=u'联系电话')
    grade = models.ForeignKey(Grade, blank=True, null=True, verbose_name=u'所教年级')
    students = models.ManyToManyField(Student, blank=True, null=True, verbose_name=u'所教学生')
    class Meta:
        ordering = ['datentry']
        verbose_name = u'教师'
        verbose_name_plural = u'教师'

    def __unicode__(self):
        return u'%s: %s, %s, %s' % (self.name, self.datentry, self.position, self.rank)


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
    teachers = models.ManyToManyField(Teacher, verbose_name=u'授课教师')
    pub_date = models.DateTimeField(default = datetime.now)
    grade = models.ForeignKey(Grade)
    klass = models.ForeignKey(KlassWiz)
    subject = models.ForeignKey(Subject)
    cinst = models.ForeignKey(Cinst)
    csort = models.ForeignKey(Csort)
    ctbgn_night = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课起始时间')
    ctend_night = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课结束时间')
    cd_night = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'上课日期')
    ctbgn_day = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课起始时间')
    ctend_day = models.TimeField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name=u'上课结束时间')
    cd_day = models.CharField(blank=True, null=True, max_length=100, verbose_name=u'上课日期')

    details = models.TextField(verbose_name=u'课程详情')
    recommend = models.BooleanField(default=False, verbose_name=u'是否推荐')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = u'课程'
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.name

class CourseTuition(models.Model):
    name = models.ForeignKey(Course)
    tuition = models.CharField(max_length=100, verbose_name=u'授课费用')
    ctimes = models.CharField(max_length=20, verbose_name=u'授课次数')

    class Meta:
        verbose_name = u'课程费用'
        verbose_name_plural = u'课程费用'

    def __unicode__(self):
        return self.tuition


class StuCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ManyToManyField(Course)
    class Meta:
        verbose_name = u'学生所学课程'
        verbose_name_plural = u'学生所学课程'
    def __unicode__(self):
        return self.student

class StuTuition(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
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

class Score(models.Model):
    student = models.ForeignKey(Student)
    tname = models.CharField(max_length=80, verbose_name=u'考试名称')
    tdate = models.DateField(editable=True, verbose_name=u'考试日期')
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
        ordering = ['tname']
    def __unicode__(self):
        return u'%s: %s' % (self.student, self.tname)



class StuRecord(models.Model):
    student = models.ForeignKey(Student)
    datefrom = models.DateField(editable=True, verbose_name=u'开始日期')
    dateto = models.DateField(editable=True, verbose_name=u'结束日期')
    stustat = models.CharField(max_length=250, verbose_name=u'学习状态')
    stugoal = models.CharField(max_length=250, verbose_name=u'学习目标')
    memo = models.CharField(blank=True, null=True, max_length=80, verbose_name=u'备注')

    class Meta:
        verbose_name = u'学习记录'
        verbose_name_plural = u'学习记录'
        ordering = ['student']
    def __unicode__(self):
        return u'%s (%s-%s) : %s-%s' % (self.student, self.datefrom, self.dateto, self.stustat, self.stugoal)





