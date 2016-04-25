#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from ci import ci_views
from sso import views
from dtr import dtr_views
from ci import pack_upload
from ci import pack_download
from ci import pack_update
from ci import pack_download_web
from ci import pack_view
from dtr import lbviews
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',views.index),
    url(r'^ci/',ci_views.ci),
    url(r'^book/$',dtr_views.Booklist.as_view()),
    url(r'^book/(\d+)',dtr_views.BookDetail.as_view()),
    url(r'^getredis/(.+)/$',dtr_views.get_redis.as_view()),
    #pack_文件上传入口
    url(r'^upload/',pack_upload.upload_file),
    #pack_web方式下载
    url(r'^download/$',pack_download_web.pack_download),
    #pack_client方式下载
    url(r'^download_client/',pack_download.pack_download),
    #pack_修改版本名
    url(r'^update/$',pack_update.pack_update),
    #pack_查看版本号并下载
    url(r'^view/',pack_view.pack_view),
    #dtr_前端路由切换视图
    url(r'^lbviews/',lbviews.lb('203.195.140.214','30000','10','10min','00').lb_list)

]
