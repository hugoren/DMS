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
# Create your views here.


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
         # url_list = Url.objects.all()
        # url_list = Url.objects.all()
        # for i in url_list:
        #     print i
        # return render(request,'index.html',{'List':select_Uri()})
        #  return  render_to_response('index.html',{'data':url_list})

        return  render(request,'ci/pull_package_version.html',{"Pack_List":pull_package_version.ssh_client("119.29.101.41","admin","y298FTgS8Y").ssh_exce_cmd()})

#
# def pack_upload(request):
#     return render(request,'ci/pack_upload.html')

def upload_file(request):
    if request.method == 'POST':

        un = request.POST.get('username')
        f = request.FILES.get('uploadfile')  #'uploadfile'与提交表单中input名一致，多个文件参见getlist()
        path = "./00"
        if not os.path.dirname(path):
            os.makedirs(path)
        filename = os.path.join('00',f.name)
        local_file = file(filename,'wb+')
        print un
        for chunk in f.chunks():
            local_file.write(chunk)
        return  HttpResponse(u'{}保存好了'.format(filename))
    return render_to_response('ci/pack_upload.html',{})

# def download_file():
#
#
# def upload_api(request):
#     url = 'http://localhost:8000/upload_api'
#     files = {'file':open('/Users/hugo/PycharmProjects/Dsso/ci/command_list','rb')}
#     r = requests.post(url,files=files)
#     print  "success"

