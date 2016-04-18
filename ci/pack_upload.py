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
        #根据文件名逐层判断文件夹是否存在
        filename_list = str(f.name).split('_')
        pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
        os.chdir(pack_path)
        if not os.path.exists(filename_list[0]):
            os.makedirs(filename_list[0])
        os.chdir(pack_path+'/'+filename_list[0])
        if not os.path.exists(filename_list[1]):
            os.makedirs(filename_list[1])
        os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1])
        if not os.path.exists(filename_list[2]):
            os.makedirs(filename_list[2])
        #流方式存包
        filename = os.path.join(pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+filename_list[2],f.name)
        try:
            local_file = file(filename,'wb+')
            for chunk in f.chunks():
                local_file.write(chunk)
            return  HttpResponse(u'{}上传成功'.format(f.name))
        except Exception as e:

            return  HttpResponse(u'{}上传失败%s'%e.message.format(f.name))
        return render_to_response('ci/pack_upload.html',{})


