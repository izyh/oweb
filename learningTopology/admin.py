# -*- coding:utf-8 -*-
from django.contrib import admin
from oweb.learningTopology.models import Node, Path
#from mezzanine.conf import register_setting
#from django.utils.translation import ugettext_lazy as _
# Register your models here.
"""
register_setting(
	name="ADMIN_MENU_ORDER",
	editable=False,
	default=(
		(_("Content"), ("pages.Page", "blog.BlogPost",
           "generic.ThreadedComment", (_("Media Library"), "fb_browse"),)),
        (_("Site"), ("sites.Site", "redirects.Redirect", "conf.Setting")),
        (_("Users"), ("auth.User", "auth.Group",)),
		(u"学习拓扑", ("Node", "Path")),
	),
)
"""
class NodeAdmin(admin.ModelAdmin):
	list_display = ["nodeName"]
	filter_horizontal = ("lastNodeList",)
	#raw_id_fields = ('nextNode',)

class PathAdmin(admin.ModelAdmin):
	list_display = ["pathName", "startNode", "endNode", "pathLength", "pathBody"]

admin.site.register(Node, NodeAdmin)
admin.site.register(Path, PathAdmin)