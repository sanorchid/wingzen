#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
#from django.utils.timezone import utc
from guestbook.forms import MsgForm
from guestbook.models import Msg
import urllib
import json

def message(request):
    ip_address = get_real_ip(request)
    #get the city of the ip.
    city_ip = get_ipinfo(ip_address)

    # get the query messages if it is not empty.
    try:
        qry_msg = Msg.objects.filter(parent_id=0).order_by('-add_date')
    except:
        qry_msg = []
    msg_lst = []
    reply_lst = []
    message = []
    mid_lst = []
    msg_dic = {}
    reply_dic = {}
    for msg in qry_msg:
        mid_lst.append(msg.id)
        msg_dic['id'] = msg.id
        msg_dic['author'] = msg.author
        msg_dic['content'] = msg.content
        msg_dic['city'] = msg.city
        msg_dic['add_date'] = msg.add_date
        msg_dic['parent_id'] = msg.parent_id

        try:
            qry_reply = Msg.objects.filter(parent_id=msg.id).order_by('add_date')
        except:
            qry_reply = []
        if qry_reply:
            for reply in qry_reply:
                reply_dic['id'] = reply.id
                reply_dic['author'] = reply.author
                reply_dic['content'] = reply.content
                reply_dic['city'] = reply.city
                reply_dic['add_date'] = reply.add_date
                reply_dic['parent_id'] = reply.parent_id
                reply_lst.append(reply_dic)

        message = (msg_dic, reply_lst)
        msg_lst.append(message)
        reply_lst = []
        msg_dic = {}
        reply_dic = {}

    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            human = True  # for captcha.
            cd = form.cleaned_data
            author = cd['author']
            content = cd['content']
            ip = ip_address
            city = city_ip
            add_date = datetime.now()
            parent_id = 0
            m = Msg(author=author, content=content, ip=ip, city=city, add_date=add_date, parent_id='0')
            m.save()
            return HttpResponseRedirect('/guestbook/')
    else:
            form = MsgForm()
    return render_to_response('guestbook/msg_list.html', {'form': form, 'object_list': msg_lst}, context_instance=RequestContext(request))


def get_real_ip(request):
    # get the visitor's real ip.
    try:
        ip_address = request.META['HTTP_X_FORWARDED_FOR']
    except KeyError:
        pass
    else:
        ip_address = ip_address.split(",")[0]
        request.META['REMOTE_ADDR'] = ip_address
    ip_address = request.META.get("REMOTE_ADDR", None)
    return ip_address

# Get the visitor's ip information.
def get_ipinfo(ip_address):
    url = r'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip_address
    page = urllib.urlopen(url)
    data = page.read()
    try:
        jsondata = json.loads(data)
    except:
        city_ip = u'地球'
    if jsondata[u'code'] == 0:
        city_ip = r'%s %s'%(jsondata[u'data'][u'country'].encode('utf-8'), jsondata[u'data'][u'city'].encode('utf-8'))
    else:
        city_ip = u'火星'
    return city_ip


