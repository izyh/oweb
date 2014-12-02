# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.core.fields import FileField
from mezzanine.utils.models import AdminThumbMixin, upload_to
from mezzanine.generic.fields import CommentsField, RatingField

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Node(Displayable, Ownable, RichText, AdminThumbMixin):
	neighbourNodes = models.ManyToManyField("self", verbose_name=u"邻居节点列表", blank=True, symmetrical=True)
	nextNode = models.ForeignKey("self", related_name="+", verbose_name=u"下级节点", blank=True, null=True)
	class Meta:
		verbose_name = u"节点"
		verbose_name_plural = u"节点"
		ordering = ("id",)
	def all_direct_previous_nodes(self):
		return self.neighbourNodes.exclude(id=self.nextNode.id).order_by("title")
	def all_next_nodes(self):
		next_node = self.nextNode
		while next_node:
			yield next_node
			next_node = next_node.nextNode
	# def get_absolute_url(self):
	# 	return "%s?n=%d" %(reverse("learn_path_detail"),self.id)

class Path(Displayable, Ownable, RichText, AdminThumbMixin):
	startNode  = models.ForeignKey("Node", verbose_name=u"路径起点", related_name="pathstart", blank=True)
	endNode    = models.ForeignKey("Node", verbose_name=u"路径终点", related_name="pathend", blank=True)
	pathLength = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"时间长度", blank=True)
	rating     = RatingField(verbose_name=_("Rating"))
	featuredImage = FileField(
		verbose_name = _("Featured Image"),
		upload_to    = upload_to("learnTopology.Path.featuredImage", "blog"),
		format       = "Image", 
		max_length   = 255, 
		null         = True,
		blank        = True)
	admin_thumb_field = "featuredImage"
	class Meta:
		verbose_name = u"路径"
		verbose_name_plural = u"路径"
		ordering = ("id",)
	def all_direct_previous_paths(self):
		pnodes = self.startNode.all_direct_previous_nodes()
		for pnode in pnodes:
			ppaths = Path.objects.filter(startNode=pnode,endNode=self.startNode)
			if len(ppaths) == 0:
				yield None
			else:
				yield ppaths[0]
	def all_next_paths(self):
		e  = self.endNode
		e0 = e.nextNode
		while e and e0:
			nps = Path.objects.filter(startNode=e,endNode=e0)
			if len(nps) == 0:
				yield None
			else:
				yield nps[0]
			e  = e0
			e0 = e.nextNode
	def get_absolute_url(self):
		return "%s?s=%d&e=%d" %(reverse("learn_path_detail"),self.startNode.id,self.endNode.id)
