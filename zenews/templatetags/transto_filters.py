#coding=utf-8
from django.template import Library

register = Library()
@register.filter
def transto(value): # Only one argument.
    'Converts a string into a custom app label , usage : string|trasto'
    l_keys = {'Auth':u'授权管理', 'Users': u'用户', 'Comments':u'评论管理','Curriculum':u'课程管理', 'Flatpages':u'简单页面管理', 'Guestbook': u'留言板管理', 'Registration': '注册信息管理', 'Sites': u'站点管理', 'Taggit': u'标签管理', 'Testbank': u'试题管理', 'Zenews': u'新闻管理', }
    r = l_keys.get(value);
    if r is None :
        r = value
    return r