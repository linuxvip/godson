#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from views import DomainListView, DomainAddView, DomainDeleteView, DomainEditView

urlpatterns = [
    url(r'^$', DomainListView.as_view(), name='domain-index'),
    url(r'^add/$', DomainAddView.as_view(), name='domain-add'),
    url(r'^delete/(?P<pk>\d+)/$', DomainDeleteView.as_view(), name='domain-delete'),
    url(r'^edit/(?P<pk>\d+)/$', DomainEditView.as_view(), name='domain-edit'),
]