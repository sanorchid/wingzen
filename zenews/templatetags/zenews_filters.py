# -*- coding: UTF-8 -*-
from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode

register = Library()
@register.filter(name='truncatehanzi', is_safe=True)
@stringfilter
def truncatehanzi(value, arg):
    """
    Truncates a string after a certain number of words including
    alphanumeric and CJK characters.

    Argument: Number of words to truncate after.
    """
    string = force_unicode(value)
    try:
        truclen = int(arg)
    except ValueError: # Invalid literal for int().
        return value # Fail silently.

    if truclen >= len(string):
        hanzi = string
    else:
        hanzi = "%s..." % string[0:truclen]
    return hanzi


