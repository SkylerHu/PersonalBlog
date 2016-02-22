# coding=utf-8

from django.conf.urls import patterns, url

urlpatterns = [
    # Examples:
    url(r'^article/list$', 'skyblog.views.article.list', name='article_list'),
    url(r'^article/(?P<article_id>\d+)$', 'skyblog.views.article.detail', name='article_detail'),

    url(r'^user/profile$', 'skyblog.views.user.my_profile', name='my_profile'),
    url(r'^links$', 'skyblog.views.user.links', name='friendly_links'),
]
