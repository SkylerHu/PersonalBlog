#!/usr/bin/env python
# coding=utf-8
import sys
import logging
import traceback
import inspect
import json

from django.conf import settings


auth_logger = logging.getLogger('auth_logger')
info_logger = logging.getLogger('info_logger')
error_logger = logging.getLogger("error_logger")
profile_logger = logging.getLogger("profile_logger")


def _get_exception_info():
    '''
    获取stacktrace
    '''
    try:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        exc = traceback.format_exception(exc_type, exc_value, exc_traceback)
        info = {'exception': '%s' % exc}
        return info
    except:
        logging.error('_get_exception_info error')
        return {}


def _get_func_args():
    '''
    获取外层函数调用参数，注意调用栈顺序，最多取最后3层调用
    '''
    try:
        stacks = inspect.stack()[:3]
        result = []
        for stack in stacks:
            item = _build_func_args_item(stack)
            result.append(item)
        return result
    except:
        logging.error('_get_func_args error')
        return []


def logging_exception():
    '''
    记录异常信息
    '''
    func_args = _get_func_args()
    exc = _get_exception_info()
    error_logger.error(_build_json_format({'stacktrace': exc, 'func_args': func_args}))
    error_logger.error(json.dumps({'stacktrace': exc, 'func_args': func_args}, ensure_ascii=True))
