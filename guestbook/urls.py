from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'guestbook.views.message'),
    )