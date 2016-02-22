#!/usr/bin/env python
# coding=utf-8
from django.db import models

from utils.date_time_util import datetime_tostr
from utils.markdown import markdown_to_html, strip_markdown_links

from skyblog.models.base import BaseModel
from skyblog.models.base import ARTICLE_STATUS, ARTICLE_TYPE
from skyblog.models.tag import Tag


class Article(BaseModel):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    title = models.CharField(verbose_name='标题', max_length=40)
    content = models.TextField(verbose_name='内容', )
    keywords = models.CharField(verbose_name='关键字', blank=True, max_length=40, help_text="输入关键字，以逗号隔开")
    status = models.IntegerField(verbose_name='状态', choices=ARTICLE_STATUS, default=ARTICLE_STATUS.SAVED)
    type = models.IntegerField(verbose_name='类型', choices=ARTICLE_TYPE, default=ARTICLE_TYPE.BLOG)
    tags = models.ManyToManyField(
            Tag,
            through='ArticleTag',
            through_fields=('article', 'tag'),
            related_name='articles',
            )

    @property
    def to_dict(self):
        return {
                'id': self.id,
                'title': self.title,
                'content': markdown_to_html(self.content),
                'summary': strip_markdown_links(self.content)[:200],
                'tags': [tag.name for tag in self.tags.all()],
                'show_title': True if self.type == ARTICLE_TYPE.BLOG else False,
                'keywords': self.keywords,
                'create_at': datetime_tostr(self.create_at),
                'update_time': datetime_tostr(self.update_time),
                }

    @classmethod
    def my_profile(cls):
        a = cls.objects.get(type=ARTICLE_TYPE.MY)
        return a.to_dict

    @classmethod
    def links(cls):
        a = cls.objects.get(type=ARTICLE_TYPE.LINK)
        return a.to_dict


class ArticleTag(BaseModel):
    class Meta:
        verbose_name = '文章标签映射'
        verbose_name_plural = '文章标签映射'

    tag = models.ForeignKey(Tag)
    article = models.ForeignKey(Article)
