from django.conf.urls.defaults import *

from zeloplus.models import Entry

entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
    'template_object_name': 'object_list',
}

entry_info_dict_m = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
    'month_format' : '%m',
}

urlpatterns = patterns('django.views.generic.date_based',
    url(r'^$', 'archive_index', entry_info_dict, 'zeloplus_entry_archive_index'),
    url(r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'zeloplus_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', entry_info_dict_m, 'zeloplus_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict_m, 'zeloplus_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict_m, 'zeloplus_entry_detail'),
)
