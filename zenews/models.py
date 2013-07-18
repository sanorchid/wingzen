#coding=utf-8
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from markdown import markdown
from taggit.managers import TaggableManager

from django.conf import settings


class LiveNewsManager(models.Manager):
    def get_query_set(self):
        return super(LiveNewsManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Category(models.Model):
    isnav = models.BooleanField(default=False) # whether to show it on navibar.
    title = models.CharField(max_length = 250, help_text = "Maximum 250 characters.")
    slug = models.SlugField(unique = True, help_text = "Suggested value automatically generated from title. Must be unique.")
    description = models.CharField(blank=True, null=True, max_length=80, verbose_name='描述')

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.title
    
    def live_news_set(self):
        from zenews.models import News
        return self.news_set.filter(status=News.LIVE_STATUS)

class News(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    # Core fields.
    title = models.CharField(max_length = 250)
    excerpt = models.TextField(blank = True)
    body = models.TextField()
    cover = models.ImageField(upload_to='newscover/%Y/%m/%d', blank=True, verbose_name='焦点图片(280*180)')
    pub_date = models.DateTimeField(default = datetime.now)

    # Fields to store generated HTML.
    excerpt_html = models.TextField(editable = False, blank = True)
    body_html = models.TextField(editable = False, blank = True)

    # Metadata.
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default = True)
    isfoc = models.BooleanField(default = False)        
    slug = models.SlugField(unique_for_date = 'pub_date')
    source = models.CharField(max_length = 250)
    status = models.IntegerField(choices = STATUS_CHOICES, default = LIVE_STATUS)

    # Categorization.
    categories = models.ManyToManyField(Category)
    tags = TaggableManager(help_text = u"标签之间用逗号分隔。")

    objects = models.Manager()
    live = LiveNewsManager()

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "news"

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(News, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return ('zenews_news_detail', (), {'year': self.pub_date.strftime("%Y"),
                                           'month': self.pub_date.strftime("%m"),
                                           'day': self.pub_date.strftime("%d"),
                                           'slug': self.slug})
    get_absolute_url = models.permalink(get_absolute_url)


# The comment moderate with akismet.
from akismet import Akismet
from django.conf import settings
from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.utils.encoding import smart_str

class NewsModerator(CommentModerator):
    auto_moderate_field = 'pub_date'
    moderate_after = 30
    email_notification = False

    def moderate(self, comment, content_object, request):
        already_moderated = super(NewsModerator, self).moderate(self, comment. content_object, request)
        if already_moderated:
            return True
        akismet_api = Akismet(key=settings.AKISMET_API_KEY,blog_url="http:/%s/"%Site.objects.get_current().domain)
        if akismet_api.verify_key():
            akismet_data = { 'comment_type': 'comment',
                             'referrer': request.META['HTTP_REFERER'],
                             'user_ip': comment.ip_address,
                             'user-agent': request.META['HTTP_USER_AGENT'] }
            return akismet_api.comment_check(smart_str(comment.comment), akismet_data, build_data=True)
        return False
moderator.register(News, NewsModerator)
