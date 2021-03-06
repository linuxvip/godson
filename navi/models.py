#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models


class navi(models.Model):
    name = models.CharField(u"名称",max_length=50)
    description = models.CharField(u"描述",max_length=50)
    url = models.URLField(u"网址")
    memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'导航管理'
        verbose_name_plural = verbose_name