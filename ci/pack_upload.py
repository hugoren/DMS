#-*-coding:utf-8-*-

#client端摸拟表单上传
import  urllib2
from  poster.encode import  multipart_encode
from  poster.streaminghttp import register_openers
from django.shortcuts import  render,render_to_response
from  django import  forms
from  django.http import  HttpResponse
import  os
import  requests
from  models import  upload_log


#接收大文件上传入口
def upload_file(request):
    if request.method == 'POST':

        # un = request.POST.get('username')
        #'uploadfile'与提交表单中input名一致，多个文件参见getlist()
        f = request.FILES.get('uploadfile')
        path = "./00"
        if not os.path.dirname(path):
            os.makedirs(path)
        filename = os.path.join('00',f.name)
        local_file = file(filename,'wb+')
        for chunk in f.chunks():
            local_file.write(chunk)
        return  HttpResponse(u'{}保存好了'.format(filename))
    return render_to_response('ci/pack_upload.html',{})


