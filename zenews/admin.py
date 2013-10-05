from django.contrib import admin
from zenews.models import Category, News

#from django.contrib.flatpages.models import FlatPage
#from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

#add tiny_mce support to flatpage.
#class FlatPageAdmin(FlatPageAdminOld):
    #class Media:
        #js = ('/static/js/tinymce/jscripts/tiny_mce/tiny_mce.js',
              #'/static/js/textareas.js',)

# We have to unregister it, and then reregister
#admin.site.unregister(FlatPage)
#admin.site.register(FlatPage, FlatPageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'the_tags', 'pub_date', 'source', 'author')
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ['title']}

    def the_tags(self, obj):
        return "%s" %(obj.tags.all(), )
    the_tags.short_description = 'tags'

admin.site.register(News, NewsAdmin)

