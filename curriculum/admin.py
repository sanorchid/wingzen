#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from curriculum.models import Course, CourseTuition, Csort, Student, SchExam, Score, StuTuition, StuRecord, Teacher
from wingoa.view_model_admin import CustomModelAdmin

#class CourseInline(admin.TabularInline):
#    model = Course

class CourseAdmin(admin.ModelAdmin):
    fieldsets=(
    	(None, {
    		'fields': ('name', 'teachers', 'pub_date', 'grade','klass', 'subject', 'inst', 'csort',)
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
    		'fields': ('details', 'is_recommended', )
    	}),    )
    filter_horizontal = ('teachers',)
    #raw_id_fields = ('teachers',)
    radio_fields = {'grade': admin.HORIZONTAL, 'klass': admin.HORIZONTAL, 'subject': admin.HORIZONTAL, 'inst': admin.HORIZONTAL, 'csort': admin.HORIZONTAL}
    list_display = ('name', 'teachers_list','inst', 'ctbgn_night', 'ctend_night', 'cd_night', 'ctbgn_day', 'ctend_day', 'cd_day', )
    # Define a custom method "teachers_list" to show the ManyToManyField "teachers" in the list_display.
    def teachers_list(self, obj):
        s = ""
        for t in obj.teachers.all():
            s += (t.staff.name)
            if t != obj.teachers.all()[len(obj.teachers.all())-1]:
                s += ', '
        return s
    teachers_list.short_description = u'教师'

    #def __init__(self, *args, **kwargs):
    #    super(CourseModelAdmin, self).__init__(*args, **kwargs)
    #    self.list_display_links=(None, )

    #def has_change_permission(self, request, obj=None):
        #if request.user.has_perm('add_course'):
        #    return True
        #self.actions=None
        #self.list_display_links = (None, )
        #return False



admin.site.register(Course, CourseAdmin)

class CourseTuitionAdmin(admin.ModelAdmin):
    list_display = ('course', 'tuition', 'ctimes')
admin.site.register(CourseTuition, CourseTuitionAdmin)

class CsortAdmin(admin.ModelAdmin):
    pass
admin.site.register(Csort, CsortAdmin)




class StudentAdmin(admin.ModelAdmin):
    #list_select_related = True
    list_display = ('name', 'sex','datentry','telephone','csort')
    filter_horizontal = ('course',)
    radio_fields = {'sex': admin.HORIZONTAL, 'grade': admin.HORIZONTAL, 'klass': admin.HORIZONTAL,'status': admin.HORIZONTAL, 'csort': admin.HORIZONTAL}
    #raw_id_fields = ('csort',)

    #readonly_fields=('name',)
    #def grade_report(self, instance):
    #    return instance.grade
    #grade_report.short_description=u'年级'
    #grade_report.allow_tags = True
    search_fields = ['name']

    #def __init__(self, *args, **kwargs):
    #    super(StudentAdmin, self).__init__(*args, **kwargs)
    #    self.actions = None
    #    self.list_display_links = (None, )

    def has_add_permission(self, request):
        in_education_group = request.user.groups.filter(name='education_grd07')
        if request.user.has_perm('add_student') or in_education_group:
            return True
        self.actions=None
        self.list_display_links = (None, )
        return False
    def has_change_permission(self, request, obj=None):
        #if not request.user.is_superuser:
        #    actions=None
        #    return False
        return True

    #def get_model_perms(self, request):
        #if request.user.is_superuser:
            #return {'view': True, 'change': True, 'add': True}
        #return {'view': True, 'change': True, 'add': False, }
    
    #def get_readonly_fields(self, request, obj=None):
     #   if not obj :
     #       return ('name',)


admin.site.register(Student, StudentAdmin)

class SchExamAdmin(admin.ModelAdmin):
    pass

admin.site.register(SchExam, SchExamAdmin)

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

    def get_queryset(self, request):
        qs = super(TeacherAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(staff__user=request.user)

admin.site.register(Teacher, TeacherAdmin)