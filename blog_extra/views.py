from __future__ import unicode_literals
from future.builtins import str
from future.builtins import int
from calendar import month_name

from django.http import Http404
from django.shortcuts import get_object_or_404

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.blog.feeds import PostsRSS, PostsAtom
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate
from mezzanine.utils.models import get_user_model

import mezzanine.blog.views

User = get_user_model()

# Create your views here.

def blog_post_detail(request, slug, year=None, month=None, day=None,
                     template="blog/blog_post_detail.html"):
    """. Custom templates are checked for using the name
    ``blog/blog_post_detail_XXX.html`` where ``XXX`` is the blog
    posts's slug.
    """
    blog_posts = BlogPost.objects.published(
                                     for_user=request.user).select_related()
    blog_post = get_object_or_404(blog_posts, slug=slug)
    context = {
    	"blog_post": blog_post,
    	"editable_obj": blog_post,
    	# extra
    	"next_blog_posts" : blog_post.related_posts.order_by("id"),
    }
    templates = [u"blog/blog_post_detail_%s.html" % str(slug), template]
    return render(request, templates, context)
