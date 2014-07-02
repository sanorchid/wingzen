from django.conf.urls import patterns, include, url
from curriculum.models import Course
from curriculum.views import CurriListView

urlpatterns = patterns('',
        url(r'^list/$', CurriListView.as_view(), name='curriculum_list'),
        url(r'^search/$', 'curriculum.views.searchCurri', name='curriculum_search'),
        url(r'^student/$', 'curriculum.views.studentList',)
)
