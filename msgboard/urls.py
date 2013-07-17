from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'msgboard.views.message'),
    )