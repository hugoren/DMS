#coding:utf-8
from  django.shortcuts import  render_to_response
from django.shortcuts import render
import  sqlite3
from  sso.models import Url

from  django.http import  HttpResponse
# Create your views here.

def select_Uri():
    url_list = Url.objects.all()
    for i in url_list:
        print i.url_name + i.url_url + i.url_note
    return url_list

def index(request):
    # return HttpResponse("欢迎hugo")
    stirng = "测试"
    List = ["1","2","3"]
    # return render(request,'index.html',{'List':List})

    #判断用户是否登陆
    if (request.user.username == '' or request.user.username ==  None):
        return render(request,'nologin.html')
    else:
         # url_list = Url.objects.all()
        # url_list = Url.objects.all()
        # for i in url_list:
        #     print i
        return render(request,'index.html',{'List':select_Uri()})
        #  return  render_to_response('index.html',{'data':url_list})
