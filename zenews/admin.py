#*-* coding: utf-8 *-*
from django.contrib import admin
from zenews.models import Category, News

from uuslug import slugify

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
    exclude = ('author', 'slug',)
    list_select_related = True
    list_filter =("categories__title", 'pub_date', 'tags__name')
    list_display = ('title', 'the_tags', 'pub_date', 'source', 'author')
    date_hierarchy = 'pub_date'
    #prepopulated_fields = {'slug': ['title']}

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(NewsAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.author.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return News.objects.all()
        return News.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.slug = slugify(obj.title, max_length=23, word_boundary=True)
        obj.save()
    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name == 'author':
            #kwargs['initial'] = request.user.id
        #return super(NewsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    def the_tags(self, obj):
        return "%s" %(obj.tags.all(), )
    the_tags.short_description = 'tags'

admin.site.register(News, NewsAdmin)

