#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
import json
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from models import domain
from forms import Domain_Form


class DomainListView(ListView):
    model = domain
    context_object_name = "domains"
    template_name = 'domain/domain_list.html'

    def get_context_data(self, **kwargs):
        context = super(DomainListView, self).get_context_data(**kwargs)
        context["temp_name"] = 'domain/domain-header.html'
        return context


class DomainAddView(CreateView):
    model = domain
    # 如果指定了form_class，则不能指定 fields
    # fields = ['name','description','url','memo']
    form_class = Domain_Form
    template_name = "domain/domain_add.html"
    success_url = reverse_lazy('domain:domain-index')

    def get_context_data(self, **kwargs):
        context = super(DomainAddView, self).get_context_data(**kwargs)
        context["temp_name"] = 'domain/domain-header.html'
        return context


class DomainDeleteView(DeleteView):
    model = domain
    # template_name = 'navi/delete_confirm.html'
    success_url = reverse_lazy('domain:domain-index')

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(DomainDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            response_data = {"results": "ok"}
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            return resp


class DomainEditView(UpdateView):
    model = domain
    form_class = Domain_Form
    template_name = "domain/domain_edit.html"
    success_url = reverse_lazy('domain:domain-index')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(DomainEditView, self).get_context_data(**kwargs)
        context["temp_name"] = 'domain/domain-header.html'
        return context
