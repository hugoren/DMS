#-*-coding:utf-8-*-

#client端摸拟表单上传

from django.shortcuts import  render,render_to_response
from django.http import HttpResponse
import os



#接收大文件上传入口
def upload_file(request):
    if request.method == 'POST':

        # un = request.POST.get('username')
        #'uploadfile'与提交表单中input名一致，多个文件参见getlist()
        f = request.FILES.get('uploadfile')
        filename_list = str(f.name).split('/')

        #获取客户传过来三个app_name,app_version,app_package参数
        app_name = request.GET.get('app_name','')
        app_version = request.GET.get('app_version','')
        app_package = str(request.GET.get('app_package','')).split('/')
        print app_name
        print app_version
        print app_package
        print '%s    %s   %s'%(app_name,app_version,app_package)
        #根据文件名逐层判断文件夹是否存在

        fisrt_layer = 'snapshot'
        pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
        os.chdir(pack_path)
        if not os.path.exists(fisrt_layer):
            os.makedirs(fisrt_layer)
        os.chdir(pack_path+'/'+fisrt_layer)
        if not os.path.exists(app_name):
            os.makedirs(app_name)
        #流方式存包
        filename = os.path.join(pack_path+'/'+fisrt_layer+'/',f.name)
        try:
            local_file = file(filename,'wb+')
            for chunk in f.chunks():
                local_file.write(chunk)
            return  HttpResponse(u'{}上传成功'.format(app_name))
        except Exception as e:

            return  HttpResponse(u'{}上传失败%s'%e.message.format(app_name))
    return render_to_response('ci/pack_upload.html',{})


