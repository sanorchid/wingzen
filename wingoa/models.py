#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    (u'M', u'男'),
    (u'F', u'女'),
    )

DEPT_CHOICES = (
	(u'ceo_office', u'总裁办公室'),
	(u'edu_dept', u'教务部'),
	(u'adm_dept', u'行政部'),
	(u'info_dept', u'信息网络处'),
	)

POSITION_CHOICES = (
	(u'ceo', u'总裁'),
	(u'manager_edu', u'教务主管'),
	(u'manager_adm', u'行政主管'),
	(u'manager_info', u'信息主管'),
	(u'officer_edu_office', u'教务办公室主任'),
	(u'officer_adm_office', u'行政办公室主任'),
	(u'director_stu_division', u'学生处处长'),
	(u'director_tch_division', u'教学处处长'),
	(u'director_resch_group', u'教研组组长'),
	(u'director_persn_division', u'人事处处长'),
	(u'director_recrt_division', u'招宣处处长'),
	(u'director_finc_division', u'财务处处长'),
	(u'director_supt_division', u'后勤处处长'),
	(u'leader_team', u'教学组组长'),
	(u'education_teacher', u'教学老师')
	)

RANK_CHOICES = (
	(u'master', u'特级教师'),
	(u'senior', u'高级教师'),
	(u'1st-grd', u'一级教师'),
	(u'2nd-grd', u'二级教师'),
	(u'3rd-grd', u'三级教师'),
	)

class Inst(models.Model):
    name = models.CharField(max_length='30', verbose_name=u'文臻校区')
    class Meta:
        verbose_name = u'文臻校区'
        verbose_name_plural = u'文臻校区'

    def __unicode__(self):
        return self.name

class KlsWing(models.Model):
    inst = models.ForeignKey(Inst, verbose_name=u'校区')
    name = models.CharField(max_length='20', verbose_name=u'文臻班级')
    room = models.CharField(max_length='30', verbose_name=u'教室地址')
    class Meta:
        verbose_name = u'文臻班级'
        verbose_name_plural = u'文臻班级'

    def __unicode__(self):
        return self.name

class Staff(models.Model):
	user = models.OneToOneField(User, verbose_name=u'用户名')
	name = models.CharField(max_length=10, verbose_name=u'职员姓名')
	sex = models.CharField(max_length=2, choices=GENDER_CHOICES, default='F', verbose_name=u'性别')
	sid = models.CharField(max_length=20, verbose_name=u'身份证号')
	birthday = models.DateField(editable=True, verbose_name=u'生日')
	graduate = models.CharField(max_length=40, verbose_name=u'毕业学校')
	major = models.CharField(max_length=20, verbose_name=u'所学专业')
	wid = models.CharField(max_length=5, verbose_name=u'职员工号')
	datentry = models.DateField(editable=True,verbose_name=u'入职日期')
	datexpire = models.DateField(editable=True,verbose_name=u'合同到期日')
	inst = models.ForeignKey(Inst, verbose_name=u'所在校区')
	department = models.CharField(max_length=15, choices=DEPT_CHOICES,verbose_name=u'所属部门')
	position = models.CharField(max_length=30, choices=POSITION_CHOICES, verbose_name=u'所属职位')
	rank = models.CharField(max_length=15, choices=RANK_CHOICES, verbose_name=u'所属级别')
	telephone = models.CharField(max_length=20, verbose_name=u'联系电话')
	is_quit = models.BooleanField(default=False, verbose_name=u'是否离职')

	def save(self, force_insert=False, force_update = False):
		super(Staff, self).save(force_insert=False, force_update=False)
		self.user.first_name = self.name
		self.user.save()



	class Meta:
		ordering = ['datentry']
		verbose_name = u'职员'
		verbose_name_plural = u'职员'

	def __unicode__(self):
		return u'%s: %s, %s, %s' % (self.name, self.datentry, self.get_position_display(), self.get_rank_display())
