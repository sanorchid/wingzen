#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from curriculum.models import Csort, GRADE_CHOICES, SUBJECT_CHOICES
from wingoa.models import Inst
class CurriSearchForm(forms.Form):
	inst = forms.ModelChoiceField(queryset=Inst.objects.all(), empty_label=None)
	csort = forms.ModelChoiceField(queryset=Csort.objects.all(), empty_label=None)
	grade = forms.ChoiceField(choices=GRADE_CHOICES)
	subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
	keywords = forms.CharField(max_length=30,required=False)
