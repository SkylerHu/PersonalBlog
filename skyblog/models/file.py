#!/usr/bin/env python
# coding=utf-8
from django.db import models

from skyblog.models.base import BaseModel, FILE_TYPE
from skyblog.models.article import Article


class FileManager(BaseModel):
    class Meta:
        verbose_name = '文件管理'
        verbose_name_plural = '文件管理'

    title = models.CharField(verbose_name='文件描述', null=True, max_length=40)
    path = models.CharField(verbose_name='文件路径', max_length=100)
    type = models.IntegerField(verbose_name='类型', choices=FILE_TYPE, default=FILE_TYPE.FILE)
