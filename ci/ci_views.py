#coding:utf-8

from django.shortcuts import render
from sso.models import Url
# from ci.pull_package_version import ssh_client
import pull_package_version
import  threading
from django.shortcuts import  render,render_to_response
from  django import  forms
from  django.http import  HttpResponse
import  os
import  requests
from  models import  upload_log


def select_Uri():
    url_list = Url.objects.all()
    print  url_list
    for i in url_list:
        print i.url_name + i.url_url + i.url_note
    return url_list


def ci(request):
    # return HttpResponse("欢迎hugo")
    stirng = "测试"
    List = ["1","2","3"]
    # return render(request,'index.html',{'List':List})

    #判断用户是否登陆
    if (request.user.username == '' or request.user.username ==  None):
        return render(request,'nologin.html')
    else:
        return  render(request,'ci/pull_package_version.html',{"Pack_List":pull_package_version.ssh_client("119.29.101.41","admin","y298FTgS8Y").ssh_exce_cmd()})

