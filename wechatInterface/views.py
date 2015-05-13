# -*- coding:utf-8 -*-
#from django.shortcuts import render
from mezzanine.utils.views import render
from django.http import HttpResponse
import hashlib, lxml, time

# Create your views here.
def wechatInterface(request):
	if request.method=="GET":
		signature=request.GET.get("signature")
		timestamp=request.GET.get("timestamp")
		nonce=request.GET.get("nonce")
		echostr=request.GET.get("echostr")
		token="zhuangyuhao"
		list=[token,timestamp,nonce]
		list.sort()
		sha1=hashlib.sha1()
		map(sha1.update,list)
		hashcode=sha1.hexdigest()
		if hashcode == signature:
			return HttpResponse(echostr)
		return HttpResponse("error!")
	elif request.method=="POST":
		xml_str=request.body
		xml=etree.fromstring(str_xml)
		toUser=xml.find("ToUserName").text
		fromUser=xml.find("FromUserName").text
		createTime=xml.find("CreateTime").text
		msgType=xml.find("MsgType").text
		#if msgType=="event":
			#content=xml.find("Event").text
			#if content=="subscribe":
		replyContent=u"欢迎使用智能硬件服务号，您将可以通过本服务号控制您的智能硬件，相关功能正在玩命开发中，敬请期待！"
		reply='''
			<xml>
			<ToUserName><![CDATA[%s]></ToUserName>
			<FromUserName><![CDATA[%s]]></FromUserName>
			<CreateTime><![CDATA[%s]]></CreateTime>
			<MsgType><![CDATA[text]]>></MsgType>
			<Content><![CDATA[%s]]></Content>
				</xml>'''%(fromUser,toUser,str(int(time.time())),replyContent)
		return HttpResponse(reply,content_type="application/xml")