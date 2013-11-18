#coding=utf-8
from django.contrib import admin
from curriculum.models import Course, CourseTuition, Csort, Cinst, Subject, Grade, KlassWiz, Student, Score, StuTuition, StuRecord, Teacher

class CourseAdmin(admin.ModelAdmin):
    fieldsets=(
    	(None, {
    		'fields': ('name', 'teachers', 'pub_date', 'grade', 'klass', 'subject', 'cinst', 'csort',)
    	}),
    	(u'晚班上课时间', {
    		'classes': ('wide',),
    		'fields': ('ctbgn_night', 'ctend_night', 'cd_night',),
    	}),
    	(u'白班上课时间', {
    		'classes': ('wide',),
    		'fields': ('ctbgn_day', 'ctend_day', 'cd_day',),
    	}),
    	(None, {
    		'fields': ('details', 'recommend', )
    	}),    )
    list_display = ('name', 'cinst', 'ctbgn_night', 'ctend_night', 'cd_night', 'ctbgn_day', 'ctend_day', 'cd_day', )
admin.site.register(Course, CourseAdmin)

class CourseTuitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'tuition', 'ctimes')
admin.site.register(CourseTuition, CourseTuitionAdmin)

class CsortAdmin(admin.ModelAdmin):
    pass
admin.site.register(Csort, CsortAdmin)

class CinstAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cinst, CinstAdmin)

class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject, SubjectAdmin)

class GradeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Grade, GradeAdmin)

class KlassWizAdmin(admin.ModelAdmin):
    pass

admin.site.register(KlassWiz, KlassWizAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)

class ScoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Score, ScoreAdmin)

class StuTuitionAdmin(admin.ModelAdmin):
    pass

admin.site.register(StuTuition, StuTuitionAdmin)

class StuRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(StuRecord, StuRecordAdmin)

class TeacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)