#! /usr/bin/env python
# coding: utf-8

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
    permission_classes = (permissions.IsAuthenticated,) # 权限检查，支持7种权限
    filter_backends = (filters.SearchFilter,)           # rest-framework 提供的默认的filters
    search_fields = ('name', 'tel')                     # 指定搜索的域,http://example.com/api/idc/?search=Azure


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer