# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from mezzanine import blog
# Create your models here.
class Node(models.Model):
	nodeName = models.CharField(max_length=50, verbose_name=u"节点名称", blank=True)
	lastNodeList = models.ManyToManyField("self", verbose_name=u"上级节点列表", blank=True, symmetrical=False)
	nextNode = models.ForeignKey("self", related_name="+", verbose_name=u"下级节点", blank=True, null=True)
	class Meta:
		verbose_name = u"节点"
		verbose_name_plural = u"节点"
		ordering = ("id",)
	def __unicode__(self):
		return self.nodeName
	def all_next_nodes(self):
		next_node = self.nextNode
		while next_node:
			yield next_node
			next_node = next_node.nextNode

class Path(models.Model):
	pathName = models.CharField(max_length=50, verbose_name=u"路径名称", blank=True)
	startNode = models.ForeignKey("Node", verbose_name=u"路径起点", related_name="pathstart", blank=True)
	endNode = models.ForeignKey("Node", verbose_name=u"路径终点", related_name="pathend", blank=True)
	pathLength = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"时间长度", blank=True)
	pathLead = models.TextField(verbose_name=u"路径指导", blank=True)
	pathBody = models.ForeignKey("blog.BlogPost", verbose_name=u"路径主体", related_name="pathbody", blank=True)
	class Meta:
		verbose_name = u"路径"
		verbose_name_plural = u"路径"
		ordering = ("id",)
	def __unicode__(self):
		return self.pathName
	def all_direct_previous_paths(self):
		pnodes = self.startNode.lastNodeList.order_by("nodeName")
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
