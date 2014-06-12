# -*- coding: UTF-8 -*-

import re
from django.utils.encoding import force_unicode
from django.utils.functional import allow_lazy

# Set up regex for alphanumeric characters
# \u00c0-\u02af: Latin
# \u0370-\u1fff: Greek and other language alphabet characters
#re_alnum = re.compile(ur'[a-zA-Z0-9\u0000-\u007f\u00c0-\u02af\u0370-\u1fff]+', re.U)
# Set up regex for hanzi
# \u3000-\ufaff: CJK characters and punctuation
#re_hanzi = re.compile(ur'[\u3000-\ufaff]+', re.U)

def len_hanzi(s):
    s = force_unicode(s)
    #length = 0
    # Length of alphanumeric characters
    #length += len(re_alnum.findall(s))
    # Length of CJK characters
    #for h in re_hanzi.findall(s):
        #length += len(h)
    return len(s)

len_hanzi = allow_lazy(len_hanzi, unicode)

def truncate_hanzi(s, num):
    s = force_unicode(s)
    trulen = int(num)
    if trulen >= len(s):
        hanzi = s
    else:
        hanzi = "%s..." % s[0:trulen]
    return hanzi

truncate_hanzi = allow_lazy(truncate_hanzi, unicode)

def demo():
    print truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 6)
    print truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 11)
    print truncate_hanzi('截取段落工具，支持English、Γρεεκ等字母语言和CJK汉字。', 20)

if __name__ == '__main__':
    demo()

