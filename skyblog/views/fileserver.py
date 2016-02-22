#!/usr/bin/env python
# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.shortcuts import render_to_response
from django.http import JsonResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.template.response import TemplateResponse

from skyblog.models import FileManager, FILE_TYPE

from utils.decorator import html_response
from utils.file_util import upload_file, get_full_path


d_dir = 'skyblog/fileserver/'


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=40)
    file = forms.FileField()
    prefix = forms.CharField(max_length=40, required=False)
    type = forms.IntegerField(widget=forms.Select(choices=FILE_TYPE))


@csrf_exempt
def upload(request):
    """
        上传图片
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            values = form.cleaned_data
            result = upload_file(file, values.get('prefix'))
            if result.get('code') == 0:
                file_path = result.get('data').get('file_path')
                file_manager = FileManager(title=values.get('title'), path=file_path, type=values.get('type'))
                file_manager.save()
                return HttpResponseRedirect('/admin/skyblog/filemanager/')
            else:
                return JsonResponse(result, encoder="utf-8")
    else:
        form = UploadFileForm()
    return TemplateResponse(request, "admin/file_add_view.html", {'form': form})
