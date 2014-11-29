# -*- coding:utf-8 -*-
from django.db import models
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
		
