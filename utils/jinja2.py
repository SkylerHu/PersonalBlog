# -*- coding: UTF-8 -*-

import re
import json
from jinja2 import Environment, Markup, evalcontextfilter, escape

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.messages.api import get_messages

from utils.date_time_util import datetime_tostr


_paragraph_re = re.compile(r'(?:\r\n|\r|\n){1}')


@evalcontextfilter
def nl2br(eval_ctx, value):
    # result = u'\n\n'.join(u'%s<br/>' % p for p in _paragraph_re.split(value))
    result = value
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        # function #####
        'static': staticfiles_storage.url,
        'url': reverse,
        'int': int,
        'datetime_tostr': datetime_tostr,
        'get_messages': get_messages,  # for message framework

        # variable #####
        'STATIC_URL': settings.STATIC_URL,
        'MEDIA_URL': settings.MEDIA_URL,
    })
    env.filters.update({
        'jsonify': lambda data: json.dumps(data),
        'nl2br': nl2br,
    })
    return env
