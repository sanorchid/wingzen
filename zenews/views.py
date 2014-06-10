from django.shortcuts import get_object_or_404, render_to_response
from django.views.generic import ArchiveIndexView, TemplateView, RedirectView, DateDetailView, ListView
from zenews.models import Category,News
from taggit.models import Tag

class NewsIndexView(ArchiveIndexView):
    queryset = News.live.all()
    date_field =  'pub_date'
    context_object_name = 'object_list'

class NewsDetailView(DateDetailView):
    queryset = News.live.all()
    date_field = 'pub_date'
    month_format = '%m'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['tag_list'] = News.tags.filter(news__slug=self.kwargs['slug'])
        return context

class CategoryListView(ListView):
    model = Category

class NewsListView(ListView):
    def get_queryset(self):
        return News.objects.filter(categories__slug__iexact=self.kwargs['slug']).order_by('-pub_date')

class TagListView(ListView):
    model = Tag

class TagView(ListView):
    def get_queryset(self):
        return News.objects.filter(tags__slug__iexact=self.kwargs['slug']).order_by('-pub_date')

def xkjl(request):
    return render_to_response('zenews/news_xkjl.html',)

