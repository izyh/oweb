#from django.shortcuts import render
from mezzanine.utils.views import render
import hashlib

# Create your views here.
def wechatInterface(request):
	signature=request.signature
	timestamp=request.timestamp
	nonce=request.nonce
	echostr=request.echostr
	token="zhuangyuhao"
	list=[token,timestamp,nonce]
	list.sort()
	sha1=hashlib.sha1()
	map(sha1.update,list)
	hashcode=sha1.hexdigest()
	
	if hashcode == signature:
		return echostr