#coding:utf-8'

from django.http import StreamingHttpResponse
import os


#web版下载
def pack_download(request):

    app_flag = request.GET.get('app_flag','')
    app_name = request.GET.get('app_name','')
    app_package = request.GET.get('app_package','')
    def file_iterator(file_name, chunk_size=512):
        print  app_package
        pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
        os.chdir(pack_path+'/'+app_flag+'/'+app_name)
        with file(app_package,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(app_package))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(app_package)

    return response




