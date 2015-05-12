#from django.shortcuts import render
from mezzanine.utils.views import render
from django.http import HttpResponse
import hashlib

# Create your views here.
def wechatInterface(request, template="wechat/wechat_auth.html"):
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