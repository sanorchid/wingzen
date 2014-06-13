from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'guestbook.views.message', name='guestbook_index'),
    )