#!/usr/bin/env python
# coding=utf-8
import datetime


def datetime_tostr(d, fmt=None):
    if not d:
        return ''
    if fmt:
        return d.strtime(fmt)
    return d.strftime('%Y-%m-%d %H:%M')


def format_timestamp(ts, fmt=None):
    if not fmt:
        fmt = '%Y-%m-%d %H:%M'
    return datetime.datetime.utcfromtimestamp(ts).strftime(fmt)


def datetime_from_str(dtstr, fmt=None):
    if not fmt:
        fmt = '%Y-%m-%d %H:%M'
    try:
        return datetime.datetime.strptime(dtstr, fmt)
    except:
        return None
