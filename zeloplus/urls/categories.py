from django.conf.urls import patterns, include, url

from zeloplus.models import Category

urlpatterns = patterns('',
        url(r'^$', 'django.views.generic.list_detail.object_list', {'queryset':Category.objects.all()}, 'zeloplus_category_list'),
        url(r'^(?P<slug>[-\w]+)/$', 'zeloplus.views.category_detail','','zeloplus_category_detail'),
)