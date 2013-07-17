from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed, FeedDoesNotExist
from django.shortcuts import get_object_or_404
from zeloplus.models import Category, Entry

current_site = Site.objects.get_current()

class LatestEntriesFeed(Feed):
    author_name = "Jason Zoe"
    copyright = "http://%s/about/" % current_site.domain
    description = "Latest entries posted to %s" % current_site.name
    link = "/"
    title = "%s: Latest entries" % current_site.name

    item_author_name = author_name

    def items(self):
        return Entry.live.all()[:15]

    def items_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.pub_date
    
    def item_categories(self, item):
        return [c.title for c in item.categories.all()]
    
    def item_guid(self, item):
        return "tag:%s, %s:%s" % (current_site.domain,
                                  item.pub_date.strftime('%Y-%m-%d'),
                                  item.get_absolute_url())

 

class CategoryFeed(LatestEntriesFeed):
    def get_object(self, request, slug):
        return get_object_or_404(Category, slug__exact=slug)
    
    def title(self, obj):
        return "%s:Latest entries in category '%s'" % (current_site.name, obj.title)
    
    def description(self, obj):
        return "%s: Latest entries in category '%s'" % (current_site.name, obj.title)
    
    def link(self, obj):
        return obj.get_absolute_url()
    
    def items(self, obj):
        return obj.live_entry_set()[:15]

