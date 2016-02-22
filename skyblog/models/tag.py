#!/usr/bin/env python
# coding=utf-8
from django.db import models

from skyblog.models.base import BaseModel


class Tag(BaseModel):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        unique_together = ('name', )

    name = models.CharField(verbose_name='名称', unique=True, max_length=10)
