from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^admin/skyblog/filemanager/add/$', 'skyblog.views.fileserver.upload', name='file_upload'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'skyblog.views.article.list', name='home'),
    url(r'^', include("skyblog.urls")),
]
