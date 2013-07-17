from django import forms

class MsgForm(forms.Form):
    author = forms.CharField(max_length=20)
    content = forms.CharField(widget=forms.Textarea)
    parent_id = forms.IntegerField(widget=forms.HiddenInput)
