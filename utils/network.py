#!/usr/bin/env python
# coding=utf-8
import json

from django.http import HttpResponse


def get_real_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']

    else:
        ip = request.META['REMOTE_ADDR']

    if ',' in ip:
        ips = ip.split(',')
        ip = ips[0]

    return ip


def has_logged_in(request):
    """check if user logged in, if not return 403 response."""
    if request.user and request.user.is_authenticated():
        return True, None

    result = {'error': 1, 'message': '未获得授权访问'}
    response = HttpResponse(status=403, content=json.dumps(result))
    return False, response

