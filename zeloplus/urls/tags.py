from django.conf.urls.defaults import *
from zeloplus.models import Entry
from tagging.models import Tag

urlpatterns = patterns('',
        url(r'^$', 'django.views.generic.list_detail.object_list', {'queryset': Tag.objects.all()}, 'zeloplus_tag_list'),
        url(r'^entries/(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list', {'queryset_or_model': Entry, 'template_name': 'zeloplus/entries_by_tag.html'}, 'zeloplus_entries_by_tag'),
)