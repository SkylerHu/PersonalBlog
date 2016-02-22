#!/usr/bin/env python
# coding=utf-8
from django.core.paginator import Paginator

from utils.decorator import html_response

from skyblog.models import Article, ARTICLE_TYPE, ARTICLE_STATUS

d_dir = 'skyblog/article/'


@html_response(d_dir + 'article_list.html')
def list(request):
    page = int(request.GET.get('page', '1'))
    page_size = 10
    articles = Article.objects.filter(type=ARTICLE_TYPE.BLOG, status=ARTICLE_STATUS.PUBLISHED)
    articles = articles.order_by('-id').all()
    if (page < 1 or (page - 1) * page_size > len(articles)):  # 不在范围内
        page = 1

    curr_page_articles = []
    for a in articles[(page-1)*page_size:page*page_size]:
        curr_page_articles.append(a.to_dict)
    paginator = Paginator(articles, page_size)
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return {'articles': curr_page_articles, 'posts': posts}


@html_response(d_dir + 'article_detail.html')
def detail(request, article_id):
    article = Article.objects.get(id=article_id).to_dict
    return {'article': article}
