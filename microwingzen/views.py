from django.http import HttpResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

import xml.etree.ElementTree as ET
import json, hashlib, time


def recdata(request):
	if request.method == 'POST':
		str_xml = request.body
		xml = ET.fromstring(str_xml)
		msgId = xml.find("MsgId").text
		content = xml.find("Content").text
		msgType = xml.find("msgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		f1 = open('f1.txt', 'w')
		f1.write("helloworld")
		f1.close()
		xml = '<xml><ToUserName><![CDATA[%s]]></ToUserName>' % from_User
		xml = '%s<FromUserName><![CDATA[%s]]></FromUserName>' % (xml, self.username)
		xml = '%s<CreateTime><![CDATA[%s]]></CreateTime>' % (xml, time.time())
		xml = '%s<MsgType><![CDATA[%s]]></MsgType>' % (xml, msgType)
		xml = '%s<Content><![CDATA[%s]]></Content>' % (xml, content)
		xml = '%s</xml>' % xml

		return HttpResponse(xml, content_type="application/xml")

class WeixinView(View):
	def __init__(self):
		self.token = 'wzwx'
		self.username = 'wzxzms'

	def get(self, request):
		data = request.GET
		signature = data.get('signature', None)
		timestamp = data.get('timestamp', None)
		nonce = data.get('nonce', None)
		echostr = data.get('echostr', None)

		ret = ''

		if self.__validate_wx(signature, timestamp, nonce, echostr):
			ret = echostr
		return HttpResponse(ret)

	def post(self, request):

		str_xml = request.body
		xml = ET.fromstring(str_xml)
		msgId = xml.find("MsgId").text
		content = xml.find("Content").text
		msgType = xml.find("msgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		f1 = open('/home/newdust/f1.txt', 'w')
		f1.write("helloworld")
		f1.close()
		xml = '<xml><ToUserName><![CDATA[%s]]></ToUserName>' % from_User
		xml = '%s<FromUserName><![CDATA[%s]]></FromUserName>' % (xml, self.username)
		xml = '%s<CreateTime><![CDATA[%s]]></CreateTime>' % (xml, time.time())
		xml = '%s<MsgType><![CDATA[%s]]></MsgType>' % (xml, msgType)
		xml = '%s<Content><![CDATA[%s]]></Content>' % (xml, content)
		xml = '%s</xml>' % xml

		return HttpResponse(xml, content_type="application/xml")

	def __validate_wx(self, signature, timestamp, nonce, echostr):
		args = [self.token, timestamp, nonce]
		args.sort()
		client_signature = hashlib.sha1(''.join(args)).hexdigest()
		if client_signature == signature:
			return True
		else:
			return False

	def replyTextMsg(self, from_User, msgType, content):
		xml = '<xml><ToUserName><![CDATA[%s]]></ToUserName>' % from_User
		xml = '%s<FromUserName><![CDATA[%s]]></FromUserName>' % (xml, self.username)
		xml = '%s<CreateTime><![CDATA[%s]]></CreateTime>' % (xml, time.time())
		xml = '%s<MsgType><![CDATA[%s]]></MsgType>' % (xml, msgType)
		xml = '%s<Content><![CDATA[%s]]></Content>' % (xml, content)
		xml = '%s</xml>' % xml

		return HttpResponse(xml, content_type="application/xml")





	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(WeixinView, self).dispatch(*args, **kwargs)


