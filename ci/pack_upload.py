#-*-coding:utf-8-*-

#client端摸拟表单上传
from django.shortcuts import  render,render_to_response
from django.http import HttpResponse
import os
import  datetime
import config_save


# def save_conf():
#     save_dir = config_save.read_conf('./conf/save_dir.conf').read_conf()
#     print save_dir
#     return save_dir

#接收大文件上传入口
def upload_file(request):
    if request.method == 'POST':

        # un = request.POST.get('username')
        #'uploadfile'与提交表单中input名一致，多个文件参见getlist()
        f = request.FILES.get('uploadfile')

        #获取客户传过来三个app_name,app_version,app_package参数
        app_name = request.GET.get('app_name','')
        app_version = request.GET.get('app_version','')
        app_package = str(request.GET.get('app_package','')).split('/')[-1]
        app_package_suffix = app_package.split('.')


        # pack_path = save_conf()
        # print  pack_path

        #生成时间戳
        T = datetime.datetime.today()
        Z = datetime.timedelta(hours=8)
        time_stamp = (T+Z).strftime("%Y%m%d%H%M")

        #存储包名
        # pack_save = '%s_%s_%s.%s.%s'%(app_name,app_version,time_stamp,app_package_suffix[1],app_package_suffix[2])
        pack_save = '%s_%s_%s_%s'%(app_name,app_version,time_stamp,app_package)

        #逐层判断目录是否存在？创建
        pack_path = config_save.read_public_conf('/Users/hugo/PycharmProjects/Dsso/ci/conf/save_dir.conf').read_conf()
        first_layer = 'snapshot'
        print pack_path
        os.chdir(pack_path)
        if not os.path.exists(first_layer):
            os.makedirs(first_layer)
        os.chdir(pack_path+'/'+first_layer)
        if not os.path.exists(app_name):
            os.makedirs(app_name)
        #流方式存包
        filename = os.path.join(pack_path+'/'+first_layer+'/'+'/'+app_name,pack_save)
        try:
            local_file = file(filename,'wb+')
            for chunk in f.chunks():
                local_file.write(chunk)
            return HttpResponse(u'{}上传成功'.format(pack_save))
        except Exception as e:

            return  HttpResponse(u'{}上传失败%s'%e.message.format(pack_save))
    return render_to_response('ci/pack_upload.html',{})


