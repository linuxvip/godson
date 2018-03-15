#! /usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from cmdb.models import Idc, Host


class IdcSerializer(serializers.ModelSerializer):
    """
    继承serializers.ModelSerializer，fields为API想要得到的字段。
    """
    class Meta:
        model = Idc
        fields = ('id', 'name', 'address', 'tel')


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('hostname', 'ip', 'sn')