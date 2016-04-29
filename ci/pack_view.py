#coding:utf-8

from django.shortcuts import render
from sso.models import Url
import  os
from django.shortcuts import render,render_to_response
import config_save

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
            pack_flag = request.POST.get("pack_version")
            #存储包的工作目录
            pack_path = config_save.read_public_conf().read_repository("repository_dir","repository")
            try:
                pack_list = os.listdir(pack_path+'/'+'/'+str(pack_flag)+'/'+str(pack_app))
                # for pack in pack_list:
                #     print  pack
                # return pack_list
                # return render(request,'ci/pack_view.html')
                download_parameter = [pack_flag,pack_app]
                return render(request,'ci/pack_view.html',{'pack_list':pack_list})
            except:
                except_list=["sorry,目录或包不存在！请重新搜索"]
                return  render(request,'ci/pack_view.html',{'pack_list':except_list})
        else:
            return render(request,'ci/pack_view.html')


