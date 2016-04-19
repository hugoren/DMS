#coding:utf-8'

from django.http import StreamingHttpResponse
import os
from  django.http import  HttpResponse


#web版下载
def pack_download(request,parameter):
    # do something...
    print parameter
    def file_iterator(file_name, chunk_size=512):
        dir_list = str(parameter).split('_')
        pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
        os.chdir(pack_path+'/'+dir_list[0]+'/'+dir_list[1]+'/'+dir_list[2])
        with file(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    # the_file_name = '/Users/hugo/PycharmProjects/Dsso/00/%s'%parameter
    response = StreamingHttpResponse(file_iterator(parameter))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(parameter)

    return response




