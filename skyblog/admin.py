#!/usr/bin/env python
# coding=utf-8
# Register your models here.
import os

from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.forms import TextInput
from django.forms.models import modelform_factory
from django.utils.safestring import mark_safe
from django.conf import settings
from django.template.response import TemplateResponse

from skyblog.models import *

from utils.file_util import get_full_path
from skyblog.views.fileserver import UploadFileForm


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('id', 'name', 'create_at')
    list_display_links = ('name', )
    fields = ('name', )


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    raw_id_fields = ('tag', )


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('id', 'title', 'status', 'tags_name', 'type')
    list_display_links = ('title', )
    inlines = [ArticleTagInline]
    fields = ('title', 'content', 'keywords', 'status', 'type')

    def tags_name(self, obj):
        tags = obj.tags.all()
        names = ', '.join([tag.name for tag in tags])
        return names
    tags_name.short_description = '相关标签'


@admin.register(FileManager)
class FileManagerAdmin(ModelAdmin):
    list_display = ('id', 'title', 'file_url', 'file_type')
    list_display_links = ('id', 'title')
    fields = ('title', 'path', 'type')

    def file_url(self, obj):
        url = get_full_path(obj.path)
        return mark_safe('<a href="{}" target="view_window">{}</a>'.format(url, url))
    file_url.short_description = '文件链接'

    def file_type(self, obj):
        return FILE_TYPE.getDesc(obj.type)
    file_type.short_description = '类型'

    def add_view(self, request):
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
            # Anything else you want in the context...
            # key=value,
            form=UploadFileForm(),
        )
        return TemplateResponse(request, "admin/file_add_view.html", context)
