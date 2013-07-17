from django.contrib import admin
from testbank.models import TagsUsed, Choice3, Choice4, Passage, EngSglChoice, EngClzChoice, EngRdhChoice1, EngRdhChoice2


class TagsUsedAdmin(admin.ModelAdmin):
    pass
admin.site.register(TagsUsed, TagsUsedAdmin)

class Choice3Admin(admin.ModelAdmin):
    pass
admin.site.register(Choice3, Choice3Admin)

class Choice4Admin(admin.ModelAdmin):
    pass
admin.site.register(Choice4, Choice4Admin)

class PassageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['body']}
admin.site.register(Passage, PassageAdmin)

class EngSglChoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(EngSglChoice, EngSglChoiceAdmin)

class EngClzChoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(EngClzChoice, EngClzChoiceAdmin)

class EngRdhChoice1Admin(admin.ModelAdmin):
    pass
admin.site.register(EngRdhChoice1, EngRdhChoice1Admin)

class EngRdhChoice2Admin(admin.ModelAdmin):
    pass
admin.site.register(EngRdhChoice2, EngRdhChoice2Admin)


