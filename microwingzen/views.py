from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json, hashlib, time

@csrf_exempt
def validate(request):
    if request.method == 'GET':
        TOKEN = 'wzwx'

        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        arglist = [TOKEN, timestamp, nonce]
        arglist.sort()
        client_signature = hashlib.sha1(''.join(arglist)).hexdigest()
        if client_signature == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("Invalid request.")
    else:
        return HttpResponse("hello world.")
