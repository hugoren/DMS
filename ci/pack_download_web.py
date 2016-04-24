#coding:utf-8
#web方式下载
from django.http import StreamingHttpResponse
import  urllib2
from  poster.encode import  multipart_encode
from  poster.streaminghttp import register_openers
from django.shortcuts import  render,render_to_response
from  django import  forms
from  django.http import  HttpResponse
import  os
import  requests
from  models import  upload_log


#web版下载
def pack_download(request):

    if request.method == 'POST':
        pack_path = "/Users/hugo/PycharmProjects/Dsso/00"
        download_file = request.POST.get('download_file')
        # pack_name = str(download_file).split('_')
        os.chdir(pack_path+'/'+'release'+'/'+'admin')
        if os.path.exists(download_file):
            def file_iterator(file_name, chunk_size=512):
                with file(file_name,'rb') as f:
                    while True:
                        c = f.read(chunk_size)
                        if c:
                            yield c
                        else:
                            break

            # the_file_name = '/Users/hugo/PycharmProjects/Dsso/00/%s'%download_file
            response = StreamingHttpResponse(file_iterator(download_file))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(download_file)
            return response
        else:
            return  HttpResponse(u'sorry,{}文不存在'.format(download_file))

    else:
         return render_to_response('ci/pack_download.html')
