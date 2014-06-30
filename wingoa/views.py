#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect

from django.db.models import Q

from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required

from wingoa.models import Staff, Inst, KlsWing
from curriculum.models import Csort, Teacher, Course, CourseTuition, Student, StuTuition, Score, StuRecord,GRADE_CHOICES
from django_bootstrap_calendar.models import CalendarEvent
#from wingoa.forms import OaAuthenticationForm

#from django.contrib.auth import authenticate, login
#from django.template import RequestContext

#from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME

'''
# permission control.
There are several sets of groups in permission control. Each set has several levels of permissions according to different ranks.
groups=['finance_director','finance_division', 'education_manager', 'education_grd7', 'education_grd8', 'education_grd9', 'education_department', 'administration_manager', 'administration_department', 'personnel_director', 'personnel_division', 'student_division',]
'''

'''
# The django.auth.views.login function
@never_cache
def login(request, extra_context=None):
    """
    Displays the login form for the given HttpRequest.
    """
    from django.contrib.auth.views import login
    context = {
        'title': u'登录',
        'app_path': request.get_full_path(),
        REDIRECT_FIELD_NAME: request.get_full_path(),
        }
    context.update(extra_context or {})

    defaults = {
        'extra_context': context,
        'current_app': 'wingoa',
        'authentication_form': OaAuthenticationForm,
        'template_name': 'wingoa/login_oa.html',
    }
    return login(request, **defaults)
'''

'''
# this view did not use the django's inner auth view.
def login_oa(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					if user.is_staff:
						login(request, user)
						return redirect('/oa/')
					else:
						messages.add_message(request, messages.INFO, u'您不是职员')
						form = LoginForm
				else:
					messages.add_message(request, messages.INFO, u'用户没有激活')
					form = LoginForm
			else:
				messages.add_message(request, messages.INFO, u'用户或密码错误')
				form = LoginForm
	else:
		form = LoginForm

	return render_to_response('wingoa/login_oa.html', {'form': form,}, context_instance=RequestContext(request))
'''

@login_required(login_url='/oa/login/')
def index_oa(request):
	if not request.user.is_staff:
		return redirect('/oa/login/')
	if not request.user.first_name:
		return redirect('/admin/wingoa/staff/add/')

	# store the number of reminders in 'num_reminder'.
	num_reminder = 0
	# store the date of today in 'today'.
	today = datetime.today().date()

	# calendar events related.
	reminder_calendar_event_deadline, reminder_calendar_event_expire = [], []
	calendar_event = CalendarEvent.objects.order_by('end')
	for one in calendar_event:
		if today + timedelta(days=15) >= one.end.date() and today < one.end.date():
			one.days = (one.end.date() - today).days
			reminder_calendar_event_deadline.append(one)
			num_reminder += 1
		elif today == one.end.date():
			reminder_calendar_event_expire.append(one)
			num_reminder += 1

	# personnel division related.
	in_personnel_division = request.user.groups.filter(name='personnel_division')
	reminder_bday_countdown, reminder_birthday = [], []
	if in_personnel_division:
		staff = Staff.objects.all()
		for one in staff:
			this_birthday = one.birthday.replace(today.year)
			if today + timedelta(days=7) >= this_birthday and today < this_birthday:
				one.days = (this_birthday - today).days
				one.this_birthday = this_birthday
				reminder_bday_countdown.append(one)
				num_reminder += 1
			elif today == this_birthday:
				reminder_birthday.append(one)
				num_reminder += 1

	# finance division related.
	in_finance_division = request.user.groups.filter(name='finance_division')
	coursetuition, stutuition = [], []
	reminder_tuition_deadline, reminder_tuition_expire = [], []
	if  in_finance_division:
		coursetuition = CourseTuition.objects.order_by('course__name')
		stutuition = StuTuition.objects.order_by('student__name', 'student__grade', '-dateto')

		#store the last stutuition item in 'one_renew' to deal with the same student with multiple stutuition items.
		one_renew = []
		for one in stutuition:
			one.student.grade = one.student.get_grade_display()
			if not one_renew or one.student != one_renew.student:
				if today + timedelta(days=7) >= one.dateto and today < one.dateto:
					one.days = (one.dateto - today).days
					reminder_tuition_deadline.append(one)
					num_reminder += 1
				elif today == one.dateto:
					reminder_tuition_expire.append(one)
					num_reminder += 1
				one_renew = one



	# education groups(grades:grd7,grd8,grd9 etc.) and student division related.
	for grd in GRADE_CHOICES:
		group_name = "education_%s" % grd[0]
		in_education_group = request.user.groups.filter(name=group_name)
		in_student_division = request.user.groups.filter(name='student_division')
		if in_education_group or in_student_division:
			course_night = Course.objects.filter(grade=group_name).order_by('ctbgn_night')
			course_day = Course.objects.filter(grade=group_name).order_by('ctbgn_day')
			student = Student.objects.filter(grade=group_name).order_by('grade')
			score = Score.objects.filter(student__grade=group_name).order_by('student__grade')
			sturecord = StuRecord.objects.filter(student__grade=group_name).order_by('student__grade')

	#teacher = Teacher.objects.order_by('grade')
	#klswing = KlsWing.objects.all()
	#csort = Csort.objects.all()
	#inst = Inst.objects.all()
	#staff = Staff.objects.all()

	return render_to_response('wingoa/index_oa.html', {
		"user": request.user,
		"reminder_bday_countdown": reminder_bday_countdown,
		"reminder_birthday": reminder_birthday,
		"reminder_tuition_deadline": reminder_tuition_deadline,
		"reminder_tuition_expire": reminder_tuition_expire,
		'reminder_calendar_event_deadline': reminder_calendar_event_deadline,
		'reminder_calendar_event_expire': reminder_calendar_event_expire,
		"num_reminder": num_reminder,
		"coursetuition": coursetuition,
		"stutuition": stutuition,
		#"teacher": teacher,
		#"klswing":klswing,
		#"csort": csort,
		#"inst": inst,
		#"staff": staff,
		},
	)

@login_required(login_url='/oa/login/')
def aget_dbsc(request):
	if not request.user.is_staff:
		return redirect('/oa/login/')
	import json
	objects_body = []
	sid = request.GET['sid']
	in_finance_division = request.user.groups.filter(name='finance_division')
	in_personnel_division = request.user.groups.filter(name='personnel_division')
	in_student_division = request.user.groups.filter(name='student_division')
	if sid == 'address-list':
		teacher = Teacher.objects.filter(staff__is_quit=False)
		for item in teacher:
			field = {}
			if in_personnel_division:
				field['pd'] = 1
				field['user'] = item.staff.user.username
				field['sid'] = item.staff.sid
				field['graduate'] = item.staff.graduate
				field['major'] = item.staff.major
				field['datentry'] = item.staff.datentry.isoformat()
				field['datexpire'] = item.staff.datexpire.isoformat()
			field['name'] = item.staff.name
			field['sex'] = item.staff.get_sex_display()
			field['birthday'] = item.staff.birthday.strftime("%m-%d")
			field['wid'] = item.staff.wid
			field['inst'] = item.staff.inst.name
			field['department'] = item.staff.get_department_display()
			field['rank'] = item.staff.get_rank_display()
			field['telephone'] = item.staff.telephone
			field['grade'] = item.get_grade_display()
			field['subject'] = item.subject

			objects_body.append(field)
	elif sid == 'present-stulist' or sid == 'trial-stulist':
		# student-list: education groups(grades:grd7,grd8,grd9 etc.) and student division related.
		if sid == 'present-stulist':
			status = "present"
		elif sid == 'trial-stulist':
			status = "trial"

		for grd in GRADE_CHOICES:
			group_name = "education_%s" % grd[0]
			in_education_group = request.user.groups.filter(name=group_name)
			if in_education_group or in_student_division:
				student = Student.objects.filter(status=status).filter(grade=grd[0]).order_by('inst')
				for item in student:
					field = {
						'name': item.name,
						'sex': item.get_sex_display(),
						'school': item.school,
						'grade': grd[1],
						'klass': item.klass,
						'telephone': item.telephone,
						'address': item.address,
						'initchs': item.initchs,
						'initmath': item.initmath,
						'initeng': item.initeng,
						'initsci': item.initsci,
						'initrnk': item.initrnk,
						'inst': item.inst.name,
						'csort': item.csort.name,
						'course': [c.name for c in item.course.all()],
						'datentry': item.datentry.isoformat(),
						'is_picked': u'是' if item.is_picked else u'否',
						'is_dining': u'是' if item.is_dining else u'否',
						'character': item.character,
						'memo': item.memo,
						'receiver': item.receiver,
						'status': item.status,


					}
					objects_body.append(field)
	elif sid == 'score-stat':
		for grd in GRADE_CHOICES:
			group_name = "education_%s" % grd[0]
			in_education_group = request.user.groups.filter(name=group_name)
			if in_education_group or in_student_division:
				score = Score.objects.filter(student__grade=grd[0]).order_by('-exam__date')
				for item in score:
					field = {
						'student': item.student.name,
						'grade': grd[1],
						'exam': item.exam.name,
						'date': item.exam.date.isoformat(),
						'english':item.english,
						'chinese': item.chinese,
						'maths': item.maths,
						'science': item.science,
						'physics': item.physics,
						'chemistry': item.chemistry,
						'biology': item.biology,
						'rank': item.rank,
						'memo': item.memo,
					}
					objects_body.append(field)


	elif sid == 'learn-record':
		for grd in GRADE_CHOICES:
			group_name = "education_%s" % grd[0]
			in_education_group = request.user.groups.filter(name=group_name)
			if in_education_group or in_student_division:
				sturecord = StuRecord.objects.filter(student__grade=grd[0]).order_by('-datefrom')
				for item in sturecord:
					field = {
						'student': item.student.name,
						'grade': grd[1],
						'datefrom': item.datefrom.isoformat(),
						'dateto': item.dateto.isoformat(),
						'stustat': item.stustat,
						'stugoal': item.stugoal,
						'is_focus':  u'是' if item.is_focus else u'否',
						'memo': item.memo,

					}
					objects_body.append(field)

	elif sid == 'zen-kls':
		klswing = KlsWing.objects.order_by('name')
		for item in klswing:
			field = {
				'inst': item.inst.name,
				'name': item.name,
				'room': item.room,
			}
			objects_body.append(field)
	elif sid == 'course-tuition':
		if in_finance_division:
			coursetuition = CourseTuition.objects.order_by('course__name')
			for item in coursetuition:
				field = {
					'name': item.course.name,
					'tuition': item.tuition,
					'ctimes': item.ctimes,
				}
				objects_body.append(field)
	elif sid == 'stu-tuition':
		if in_finance_division:
			stutuition = StuTuition.objects.filter(Q(student__status='trial') | Q(student__status='present')).order_by('student__name')
			for item in stutuition:
				field = {
					'student': item.student.name,
					'grade':item.student.get_grade_display(),
					'course': item.course.name,
					'datefrom': item.datefrom.isoformat(),
					'dateto': item.dateto.isoformat(),
					'tuition': item.tuition,
					'memo': item.memo,
				}
				objects_body.append(field)

	objects_head = {"success": 1}
	objects_head["result"] = objects_body
	return HttpResponse(json.dumps(objects_head, encoding='utf-8'), content_type="application/json")







