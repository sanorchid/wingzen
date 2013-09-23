#coding=utf-8
from django import forms
from captcha.fields import CaptchaField

class MsgForm(forms.Form):
    author = forms.CharField(label=u'称呼', max_length=20)
    content = forms.CharField(label=u'内容', widget=forms.Textarea)
    captcha = CaptchaField(label=u'验证码')
   # parent_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
