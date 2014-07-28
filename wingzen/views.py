from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from datetime import datetime
from zenews.models import Category, News
from curriculum.models import Course, GRADE_CHOICES, SUBJECT_CHOICES
from curriculum.forms import CurriSearchForm

def topnav():
    navitem = Category.objects.filter(isnav=True).order_by('title')
    return navitem

def index(request):
    focpic = News.objects.filter(isfoc=True).order_by('-pub_date')[:6]
    navitem = topnav()
    recrs = Course.objects.filter(is_recommended=True).order_by('-pub_date')[:6]
    prs_month = datetime.now().month

    form = CurriSearchForm()

    return render(request, 'index.html',
                            {'navitem': navitem, 'focpic': focpic,'recrs': recrs, 'prs_month': prs_month, 'grade': GRADE_CHOICES, 'subject': SUBJECT_CHOICES, 'form': form}
    )

import json, hashlib, time

def validate(request):
    TOKEN = 'wzwx'
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    params = {'token':TOKEN, 'timestamp': timestamp, 'nonce':nonce}
    echostr = request.GET['echostr']

    if params:
        sort_params = sorted([v for k,v in params.items()])
        client_signature = hashlib.sha1(''.join(sort_params)).hexdigest()

        if client_signature == signature:
            return echostr
    return False





def test(request):
    focpic = News.objects.filter(isfoc=True).order_by('-pub_date')[:6]
    navitem = Category.objects.filter(isnav=True).order_by('title')
    recrs = Course.objects.filter(is_recommended=True).order_by('-pub_date')[:6]
    prs_month = datetime.now().month
    return render_to_response('tma.html',
                            {'navitem': navitem, 'focpic': focpic,'recrs': recrs, 'prs_month': prs_month, 'grade': GRADE_CHOICES, 'subject': SUBJECT_CHOICES}
    )

