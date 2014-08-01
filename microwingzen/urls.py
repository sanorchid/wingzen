#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'microwingzen.views.validate', name='mwzv'),
)

