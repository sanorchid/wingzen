#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from guardian.admin import GuardedModelAdmin
from wingoa.models import Staff, Inst, KlsWing
from django.contrib.auth.models import User

from django.contrib.admin.sites import AdminSite

#AdminSite.login_template = "wingoa/login_oa.html"

class InstAdmin(admin.ModelAdmin):
    #inlines = [
    #    CourseInline,
    #]
    pass
admin.site.register(Inst, InstAdmin)

class KlsWingAdmin(admin.ModelAdmin):
    pass

admin.site.register(KlsWing, KlsWingAdmin)

class StaffAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex', 'wid', 'sid', 'birthday', 'position', 'telephone')

	search_fields = ['name', ]

	#def staff_name(self, obj):
	#	return "%s%s" % (obj.user.last_name, obj.user.first_name)
	#staff_name.short_description = u'姓名'

	#readonly_fields=('show_name',)
	#def show_name(self, obj):
	#	return "%s%s" % (obj.user.last_name, obj.user.first_name)
	#show_name.short_description=u'姓名显示'
	#show_name.allow_tags = True
	
	#def has_add_permission(self, request):
	#	if request.user.is_superuser:
	#		return True
	#	return False
	
	#def has_delete_permission(self, request):
	#	if request.user.is_superuser:
	#		return True
	#	return False
	
	def get_queryset(self, request):
		qs = super(StaffAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if not request.user.is_superuser:
			if db_field.name == "user":
				kwargs["queryset"] = User.objects.filter(username=request.user)
		return super(StaffAdmin,self).formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Staff,StaffAdmin)


