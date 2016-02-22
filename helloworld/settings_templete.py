#!/usr/bin/env python
# coding=utf-8
from helloworld.base_settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 设置为mysql数据库
        'NAME': 'backend',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
            "charset": "utf8mb4",  # 为了支持emoji表情
        },
    },

}

# 七牛配置
QINIU_ACCESS_KEY = ""
QINIU_SECRET_KEY = ""
QINIU_HOST = ""
QINIU_SCOPE = ""
