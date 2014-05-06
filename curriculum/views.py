#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import ArchiveIndexView, TemplateView, RedirectView, DateDetailView, ListView
from curriculum.models import Course, Student

class CurriIndexView(ArchiveIndexView):
    queryset = Course.objects.filter(is_recommended=True).all()
    date_field =  'pub_date'
    context_object_name = 'object_list'

class CurriDetailView(DateDetailView):
    queryset = Course.objects.all()
    date_field = 'pub_date'
    month_format = '%m'

class CurriListView(ListView):
    template_name = 'curriculum/base_curriculum.html'
    def get_queryset(self):
        currilist = Course.objects.order_by('-pub_date')
        return currilist

@login_required
def studentList(request):
    stulist = Student.objects.filter(grade_id__name=u'七年级').order_by('spell')
    return render_to_response('curriculum/stumanage.html', {'stulist':stulist,}
    )



