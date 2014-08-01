from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

import xml.etree.ElementTree as ET
import json, hashlib, time

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
		content = xml.find("Content").text
		msgType = xml.find("msgType").text
		fromUser = xml.find("FromUserName").text
		toUser = xml.find("ToUserName").text
		ft=[content,msgType,fromUser,toUser]
		f1 = open('f1.txt', 'w')
		f1.write(ft)
		f1.close()
		response = self.replyTextMsg(self, from_User, msgType, content)

		return response

	def __validate_wx(self, signature, timestamp, nonce, echostr):
		args = [self.token, timestamp, nonce]
		args.sort()
		client_signature = hashlib.sha1(''.join(args)).hexdigest()
		if client_signature == signature:
			return True
		else:
			return False

	def replyTextMsg(self, from_User, msgType, content):
		xml = '<xml><ToUserName>%s</ToUserName>' % from_User
		xml = '%s<FromUserName>%s</FromUserName>' % (xml, self.username)
		xml = '%s<CreateTime>%s</CreateTime>' % (xml, time.time())
		xml = '%s<MsgType>%s</MsgType>' % (xml, msgType)
		xml = '%s<Content>%s</Content>' % (xml, content)
		xml = '%s</xml>' % xml

		return HttpResponse(xml, content_type="application/xml")





	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(WeixinView, self).dispatch(*args, **kwargs)


