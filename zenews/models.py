#coding=utf-8
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from markdown import markdown
from taggit.managers import TaggableManager

from django.conf import settings

from redactor.fields import RedactorField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class LiveNewsManager(models.Manager):
    def get_query_set(self):
        return super(LiveNewsManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Category(models.Model):
    isnav = models.BooleanField(default=False, verbose_name='是否显示在导航栏') # whether to show it on navibar.
    title = models.CharField(max_length = 250, help_text = "最多120个字",  verbose_name='标题')
    slug = models.SlugField(unique = True, help_text = "使用英文字母，显示在地址栏，用于区别网址，必须唯一。",  verbose_name='唯一标识符')
    description = models.CharField(blank=True, null=True, max_length=80, verbose_name='描述')

    class Meta:
        verbose_name = '类目'
        verbose_name_plural = '类目'
        ordering = ['title']

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
    title = models.CharField(max_length = 250,  verbose_name='标题')
    excerpt = models.TextField(blank = True,  verbose_name='摘要')
    body = RedactorField(verbose_name='内容')
    cover = models.ImageField(upload_to='newscover/%Y/%m/%d', blank=True, verbose_name='焦点图片')
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[ResizeToFill(285,180)],
                                     format='JPEG',
                                     options={'quality':80})
    pub_date = models.DateTimeField(default = datetime.now,  verbose_name='发表日期')

    # Fields to store generated HTML.
    excerpt_html = models.TextField(editable = False, blank = True)
    body_html = models.TextField(editable = False, blank = True)

    # Metadata.
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  verbose_name='作者')
    enable_comments = models.BooleanField(default = True,  verbose_name='是否允许评论')
    isfoc = models.BooleanField(default = False,  verbose_name='是否焦点新闻')
    slug = models.SlugField(unique_for_date = 'pub_date', verbose_name='唯一标识符')
    source = models.CharField(max_length = 250, verbose_name='来源')
    status = models.IntegerField(choices = STATUS_CHOICES, default = LIVE_STATUS, verbose_name='新闻稿状态')

    # Categorization.
    categories = models.ManyToManyField(Category, verbose_name='新闻分类')
    tags = TaggableManager(help_text = u"标签之间用空格分隔。", verbose_name='新闻标签')
    # 新闻中填写标签时有bug，即有些中文字的slug会空着导致显示标签时出错
    objects = models.Manager()
    live = LiveNewsManager()

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'
        ordering = ['-pub_date']

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
from fluent_comments.moderation import moderate_model
from zenews.models import News

moderate_model(News,
    publication_date_field='pub_date',
    enable_comments_field='enable_comments',
)

