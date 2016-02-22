#!/usr/bin/env python
# coding=utf-8
import datetime
from django.db import models

from utils.enumeration import Enumeration


# -------枚举start----##################################
# 博客状态
ARTICLE_STATUS = Enumeration([
        (0, 'SAVED', '已保存'),
        (1, 'PUBLISHED', '已发布'),
    ])
ARTICLE_TYPE = Enumeration([
        (0, 'BLOG', '博客'),
        (1, 'MY', '个人介绍'),
        (2, 'LINK', '友情链接'),
    ])
FILE_TYPE = Enumeration([
        (1, 'IMAGE', '图片'),
        (2, 'GIF', 'gif'),
        (3, 'AUDIO', '语音'),
        (0, 'FILE', '文件'),
    ])
# =======枚举end====#####################################


# 基类
class BaseModel(models.Model):
    class Meta:
        abstract = True

    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
