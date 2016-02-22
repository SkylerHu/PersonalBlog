#!/usr/bin/env python
# coding=utf-8
import os
import hashlib
import datetime
import json
import urllib
import time

from django.conf import settings

from qiniu import Auth
from qiniu import put_data

from utils.log_util import error_logger


def _upload_file_name(tempfilename, prefix=None):
    if not tempfilename:
        return None
    if not prefix:
        prefix = datetime.datetime.today().strftime("%Y/%m/%d")
    md5 = hashlib.md5(str(time.time()).encode("utf8")).hexdigest()[:10]
    md5 = prefix + '/' + md5
    shotname, extension = os.path.splitext(tempfilename)
    if extension:
        md5 = '{}{}'.format(md5, extension)
    return md5


def upload_file(file, prefix=None):
    q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
    token = q.upload_token(settings.QINIU_SCOPE)

    file_name = _upload_file_name(file.name, prefix)
    response = put_data(
            token,
            file_name,
            file,
            params=None,
            mime_type='application/octet-stream',
            check_crc=False,
            progress_handler=None,
        )
    if response and response[0].get('key'):
        key = response[0].get('key')
        return {'code': 0, 'message': '上传成功', 'data': {'file_path': key}}
    else:
        error_logger.error('qiniu==>response: %s' % json.dumps(response))
        return {'code': 1, 'message': '上传失败，请重试', 'data': response}


def get_full_path(path_name, extra=''):
    if not path_name:
        return None
    full_path = urllib.parse.urljoin(settings.QINIU_HOST, path_name)
    return full_path + extra
