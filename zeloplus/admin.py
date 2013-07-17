from django.contrib import admin
from zeloplus.models import Category, Entry

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld

class FlatPageAdmin(FlatPageAdminOld):
    class Media:
        js = ('/sitemedia/js/tinymce/jscripts/tiny_mce/tiny_mce.js',
              '/sitemedia/js/textareas.js',)

# We have to unregister it, and then reregister
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags', 'pub_date', 'author')
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ['title']}
    class Media:
        js = (
            '/sitemedia/js/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/sitemedia/js/textareas.js',
        )
admin.site.register(Entry, EntryAdmin)

