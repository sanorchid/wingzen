from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
#from django.utils.timezone import utc
from msgboard.forms import MsgForm
from msgboard.models import Msg


def message(request):
    ip_address = request.META['REMOTE_ADDR']
    qry_msg = Msg.objects.filter(parent_id=0).order_by('-add_date')
    msg_lst = []
    reply_lst = []
    #message = []
    mid_lst = []
    msg_dic = {}
    reply_dic = {}
    for msg in qry_msg:
        mid_lst.append(msg.id)
        msg_dic['id'] = msg.id
        msg_dic['author'] = msg.author
        msg_dic['content'] = msg.content
        msg_dic['ip'] = msg.ip
        msg_dic['add_date'] = msg.add_date
        msg_dic['parent_id'] = msg.parent_id

        qry_reply = Msg.objects.filter(parent_id=msg.id).order_by('add_date')
        if qry_reply:
            for reply in qry_reply:
                reply_dic['id'] = reply.id
                reply_dic['author'] = reply.author
                reply_dic['content'] = reply.content
                reply_dic['ip'] = reply.ip
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
            cd = form.cleaned_data
            author = cd['author']
            content = cd['content']
            ip = ip_address
            add_date = datetime.now()
            parent_id = 0
            m = Msg(author=author, content=content, ip=ip, add_date=add_date, parent_id='0')
            m.save()
            return HttpResponseRedirect('/msgboard/')
    else:
            form = MsgForm()
    return render_to_response('msgboard/msg_list.html', {'form': form,'message':message, 'qry_msg':qry_msg, 'object_list': msg_lst, 'qry_reply':qry_reply, 'msg_dic':msg_dic,'reply_dic':reply_dic,'reply_lst':reply_lst,'mid_lst':mid_lst}, context_instance=RequestContext(request))
    
        

# Get the visitor's ip address.
def get_remote_addr(request):
    try:
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
    except:
        pass


