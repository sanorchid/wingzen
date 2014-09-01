# *-* coding: utf-8 *-*

from django.contrib import admin
from spirit.models import Topic

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Topic, TopicAdmin)