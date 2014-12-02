from __future__ import unicode_literals
from django.conf.urls import patterns, url
from mezzanine.conf import settings

urlpatterns = patterns("learningTopology.views",
    # url("^(?P<slug>.*)$" , "learn_path_detail"),
    url("^path/$" , "learn_path_detail", name="learn_path_detail"),
)
