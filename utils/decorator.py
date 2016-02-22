#!/usr/bin/env python
# coding=utf-8
from functools import wraps

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def login_required(view_func):
    pass


def json_http_response(result, status=200):
    return JsonResponse(result, encoder="utf-8")


def html_response(tpl):
    def _html_response(fn):
        @wraps(fn)
        def wrapper(request, *args, **kwargs):
            try:
                data = fn(request, *args, **kwargs)
                if settings.DEBUG and request.GET.get('debug'):
                    return json_http_response(data)
                if isinstance(data, HttpResponse):
                    return data
                return render(request, tpl, data)
            except:
                raise
        return wrapper
    return _html_response
