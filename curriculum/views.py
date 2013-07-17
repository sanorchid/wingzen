from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import ArchiveIndexView, TemplateView, RedirectView, DateDetailView, ListView
from curriculum.models import Course

class CurriIndexView(ArchiveIndexView):
    queryset = Course.objects.filter(recommend=True).all()
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



