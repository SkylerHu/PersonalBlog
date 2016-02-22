#!/usr/bin/env python
# coding=utf-8

from utils.decorator import html_response

from skyblog.models import Article
from skyblog.views.article import d_dir as article_d_dir

d_dir = 'skyblog/user/'


@html_response(article_d_dir + 'article_detail.html')
def my_profile(request):
    """
        我的简介
    """
    article = Article.my_profile()
    return {'article': article}


@html_response(article_d_dir + 'article_detail.html')
def links(request):
    article = Article.links()
    return {'article': article}
