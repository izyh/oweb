from __future__ import unicode_literals
from django.conf.urls import patterns, url
from mezzanine.conf import settings

urlpatterns = patterns("wechatInterface.views",
    url("^auth/$" , "wechatInterface", name="wechatInterface"),
)
