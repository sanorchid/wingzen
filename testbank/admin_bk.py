from django.contrib import admin
from testbank.models import TagsUsed, ChoiceIndependent, ChoiceDependent, ChoiceMatch, Passage,ProblemDependent, ProblemIndependent, BlankContext, FillContent


class TagsUsedAdmin(admin.ModelAdmin):
    pass
admin.site.register(TagsUsed, TagsUsedAdmin)

class ChoiceIndependentAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChoiceIndependent, ChoiceIndependentAdmin)

class ChoiceDependentAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChoiceDependent, ChoiceDependentAdmin)

class ChoiceMatchAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChoiceMatch, ChoiceMatchAdmin)

class PassageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Passage, PassageAdmin)

class ProblemDependentAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProblemDependent, ProblemDependentAdmin)

class ProblemIndependentAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProblemIndependent, ProblemIndependentAdmin)

class BlankContextAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlankContext, BlankContextAdmin)

class FillContentAdmin(admin.ModelAdmin):
    pass
admin.site.register(FillContent, FillContentAdmin)



