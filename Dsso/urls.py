#coding:utf-8
"""Dsso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ci import ci_views
from sso import  views
from dtr import  dtr_views
from ci import  pack_upload
from ci import  pack_download
from ci import  pack_update
from ci import  pack_download_web
from ci import  pack_view
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
    url(r'^download_client/(.+)/$',pack_download.pack_download),
    #pack_修改版本名
    url(r'^update/(.+)/(.+)/$',pack_update.pack_update),
    #pack_查看版本号并下载
    url(r'^view/',pack_view.pack_view),

]
