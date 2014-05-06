from django.contrib import admin
from django_bootstrap_calendar.models import CalendarEvent

class CalendarEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(CalendarEvent, CalendarEventAdmin)
