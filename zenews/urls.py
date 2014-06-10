from django.conf.urls import patterns, include, url
from zenews.models import News
from zenews.views import  NewsIndexView, NewsDetailView, CategoryListView, NewsListView, TagListView, TagView

urlpatterns = patterns('',
        #url(r'^tags/(?P<slug>[-\w]+)/$', 'taggit.views.tagged_object_list', {'queryset': News.live.all(), 'template_name': 'zenews/news_by_tag.html'}, name='zenews_news_by_tag'),
        url(r'^xkjl/$', 'zenews.views.xkjl',),
        url(r'^tags/(?P<slug>[-\w]+)/$', TagView.as_view(), name='zenews_news_by_tag'),
        url(r'^tags/$', TagListView.as_view(), name='zenews_tag_list'),
        url(r'^categories/$', CategoryListView.as_view(), name='zenews_category_list'),
        url(r'^$', NewsIndexView.as_view(), name='zenews_news_archive_index'),
        url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='zenews_news_detail'),
        url(r'^categories/(?P<slug>[-\w]+)/$', NewsListView.as_view(), name='zenews_news_list'),
)

urlpatterns += patterns('',
	url(r'^comments/', include('fluent_comments.urls')),
)