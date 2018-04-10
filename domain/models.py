#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db import models

# ADD_AREA = (
#     (str(1), u"dnspod"),
#     (str(2), u"company-dns"),
#     (str(3), u"azure-dnsmasq")
#     )

ADD_AREA = (
    ("dnspod", u"dnspod"),
    ("company-dns", u"company-dns"),
    ("azure-dnsmasq", u"azure-dnsmasq")
    )


class domain(models.Model):
    domain_name = models.URLField(u"域名名称")
    applicant = models.CharField(u"申请人",max_length=50)
    usage = models.CharField(u"用途",max_length=50)
    env = models.CharField(u"使用环境", max_length=50, null=True, blank=True)
    ip = models.GenericIPAddressField(u"解析IP", max_length=15)
    add_area = models.CharField(u"添加位置", choices=ADD_AREA, max_length=30, null=True, blank=True)
    add_time = models.DateTimeField(u"添加时间", max_length=200, null=True, blank=True)
    expiration_time = models.DateTimeField(u"过期时间", max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.domain_name

    class Meta:
        verbose_name = u'域名管理'
        verbose_name_plural = verbose_name