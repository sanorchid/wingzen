#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from microwingzen.views import WeixinView

urlpatterns = patterns('',
	#url(r'^$', WeixinView.as_view(), ),
	url(r'^$', 'microwingzen.views.recdata',),
)

