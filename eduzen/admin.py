from django.contrib import admin
from eduzen.models import Grade, Student, Score, Tuition, Staff

class GradeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Grade, GradeAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)

class ScoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Score, ScoreAdmin)

class TuitionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tuition, TuitionAdmin)

class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff, StaffAdmin)