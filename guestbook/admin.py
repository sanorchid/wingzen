from django.contrib import admin
from guestbook.models import Msg

class MsgAdmin(admin.ModelAdmin):
    list_display = ('add_date', 'content', 'author')
    date_hierarchy = 'add_date'

admin.site.register(Msg, MsgAdmin)

