#!/usr/bin/env python
# coding=utf-8
from functools import wraps

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

from utils.log_util import auth_logger


def json_http_response(fn):
    @wraps(fn)
    def wrapper(request, *args, **kwargs):
        data = fn(request, *args, **kwargs)
        return JsonResponse(data, safe=False)
    return wrapper


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


def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user and request.user.is_authenticated():
            return view_func(request, *args, **kwargs)

        else:
            if 'app_name' not in request.GET:
                # access from web
                login_url = reverse('django.contrib.auth.views.login')
                url = '%s?next=%s' % (login_url, request.get_full_path())
                return redirect(url)

            result = {'error': 1, 'message': '未获得授权访问'}
            request_data = {key: value for key, value in request.REQUEST.iteritems()}
            session_data = {key: value for key, value in request.session.iteritems()}
            error_data = {'request': request_data, 'session': session_data}
            # 打印错误日志
            auth_logger.error(json.dumps(error_data))

            response = HttpResponse(status=403, content=json.dumps(result))
            return response

    return _wrapped_view


def group_required(group_id):
    """
    放到view上的装饰器，限制只能属于某一组的用户或者管理员访问，否则返回Forbidden
    :param group_id: UserGroup ID
    :return:
    """
    def deco(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user and request.user.is_authenticated():
                if request.user.is_superuser or request.user.groups.filter(id=group_id).exists():
                    return view_func(request, *args, **kwargs)

            return HttpResponseForbidden()
        return _wrapped_view
    return deco
