#coding:utf-8

from django.shortcuts import render
from sso.models import Url
import  os
from django.shortcuts import render,render_to_response


def pack_view(request):
    # return HttpResponse("欢迎hugo")
    stirng = "测试"
    List = ["1","2","3"]
    # return render(request,'index.html',{'List':List})

    #判断用户是否登陆
    if (request.user.username == '' or request.user.username ==  None):
        return render(request,'nologin.html')
    else:
        if request.method == 'POST':

            #获取form端参数
            # pack_env = request.POST.get("pack_env")
            pack_app = request.POST.get("pack_app")
            pack_version = request.POST.get("pack_version")

            pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
            pack_list = os.listdir(pack_path+'/'+'/'+str(pack_version)+'/'+str(pack_app))
            # for pack in pack_list:
            #     print  pack
            # return pack_list
            # return render(request,'ci/pack_view.html')
            pack_list
            return render(request,'ci/pack_view.html',{'pack_list':pack_list})
        else:
            return render(request,'ci/pack_view.html')


