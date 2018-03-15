#! /usr/bin/env python
# coding: utf-8

import django_filters
from rest_framework import viewsets, filters, permissions
from rest_framework.exceptions import APIException

from .models import Host, Idc
from .serializers import IdcSerializer, HostSerializer


# class IdcnameFilter(filters.BaseFilterBackend):
#     """
#     根据 idc name 来删选
#     """
#
#     def filter_queryset(self, request, queryset, view):
#         idc_name = request.QUERY_PARAMS.get('idc_name')
#         if idc_name:
#             return queryset.filter(idcname=idc_name)
#         else:
#             #return queryset
#             raise FilterError
#
#
# class FilterError(APIException):
#     status_code = 406
#     default_detail = 'Query arguments error!'


class IdcViewSet(viewsets.ModelViewSet):
    """
    queryset设置为Model的queryset，serializer_class设置为刚才定义的serializer。
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # filter_backends = (IdcnameFilter,)


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer