from django.contrib import admin
from curriculum.models import Course, Csort, Cinst, Subject

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)

class CsortAdmin(admin.ModelAdmin):
    pass

admin.site.register(Csort, CsortAdmin)

class CinstAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cinst, CinstAdmin)

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)