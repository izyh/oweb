from __future__ import unicode_literals
from django.conf.urls import patterns, url
from mezzanine.conf import settings

# Leading and trailing slahes for urlpatterns based on setup.
_slashes = (
    "/" if settings.BLOG_SLUG else "",
    "/" if settings.APPEND_SLASH else "",
)

urlpatterns = patterns('blog_extra.views',
    url("^%s(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/"
        "(?P<slug>.*)%s$" % _slashes,
        "blog_post_detail", name="blog_post_detail_day"),

    url("^%s(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>.*)%s$" % _slashes,
        "blog_post_detail", name="blog_post_detail_month"),

    url("^%s(?P<year>\d{4})/(?P<slug>.*)%s$" % _slashes,
        "blog_post_detail", name="blog_post_detail_year"),

    url("^%s(?P<slug>.*)%s$" % _slashes, "blog_post_detail",
        name="blog_post_detail"),
)
