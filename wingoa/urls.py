#coding=utf-8
from django.conf.urls import patterns, include, url
#from django.views.generic import TemplateView

#from wingoa.models import *
#from wingoa.views import *
#from django.contrib.auth import views as auth_views
from wingoa.forms import OaAuthenticationForm
#from django.template import RequestContext

urlpatterns = patterns('',
        url(r'^$', 'wingoa.views.index_oa',name='index_oa'),
        #url(r'^login/$', 'wingoa.views.login', name='login_oa'),
        url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'wingoa/login_oa.html','authentication_form': OaAuthenticationForm,}, name='login_oa'),
        url(r'^logout/$', 'django.contrib.auth.views.logout',{'template_name':'wingoa/login_oa.html', 'extra_context':{'msg_logout':u'您已注销。'}}, name='logout_oa'),
        url(r'^aget_dbsc/$', 'wingoa.views.aget_dbsc', name='aget_dbsc'),
)