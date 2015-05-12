from __future__ import unicode_literals
from future.builtins import str
from future.builtins import int
from calendar import month_name

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.blog.feeds import PostsRSS, PostsAtom
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate
from mezzanine.utils.models import get_user_model

from learningTopology.models import Path, Node

def learn_path_detail(request, template="learn/path_detail.html"):
	return HttpResponse("ok")
	s = request.GET['s']
	e = request.GET['e']
	try:
		path_detail = Path.objects.filter(startNode=s,endNode=e)[0]
		context = {
			"path_detail" : path_detail,
		}
		templates = [template]
		return render(request, templates, context)
	except IndexError :
		raise Http404

def echo(request):
	return HttpResponse('hello')