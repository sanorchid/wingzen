#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
	# url for bootstrap test.
	url(r'^test/', 'wingzen.views.test'),

    url(r'^$', 'wingzen.views.index'),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^curriculum/', include('curriculum.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^news/', include('zenews.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^oa/', include('wingoa.urls')),
    url(r'^calendar/', include('django_bootstrap_calendar.urls')),
    url(r'^bbs/', include('spirit.urls', namespace="spirit", app_name="spirit")),
    url(r'^weixin/', include('microwingzen.urls')),
) + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
