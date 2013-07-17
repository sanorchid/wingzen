from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import datetime
from zenews.models import Category, News
from curriculum.models import Course

def index(request):
    focpic = News.objects.filter(isfoc=True).order_by('-pub_date')[:6]
    navitem = Category.objects.filter(isnav=True).order_by('title')
    recrs = Course.objects.filter(recommend=True).order_by('-pub_date')[:6]
    prs_month = datetime.now().month
    return render_to_response('index.html', 
                            {'navitem': navitem, 'focpic': focpic,'recrs': recrs, 'prs_month': prs_month, }
    )


