#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.widgets import *
from .models import domain


class Domain_Form(forms.ModelForm):
    def clean(self):
        cleaned_data = super(Domain_Form, self).clean()
        value = cleaned_data.get('domain_name')
        try:
            domain.objects.get(domain_name=value)
            self._errors['domain_name'] = self.error_class(["%s的信息已经存在" % value])
        except domain.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = domain
        exclude = ("id",)
        widgets = {
            'domain_name': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'ip': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'必填项'}),
            'usage': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'applicant': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'env': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'add_area': Select(attrs={'class': 'form-control', 'style': 'width:530px;'}),
            'add_time': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;','placeholder': u'添加时间 yyyy-mm-dd'}),
            'expiration_time': TextInput(attrs={'class': 'form-control', 'style': 'width:530px;', 'placeholder': u'到期时间 yyyy-mm-dd'}),

        }
