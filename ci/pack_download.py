#coding:utf-8'

from django.http import StreamingHttpResponse
import os
import time
import stat


#


def pack_download(request):

    app_flag = request.GET.get('app_flag','')
    app_name = request.GET.get('app_name','')
    app_package = request.GET.get('app_package','')
    pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
    DIR = pack_path+'/'+app_flag+'/'+app_name
    def pack_compare(x, y):
        stat_x = os.stat(DIR + "/" + x)
        stat_y = os.stat(DIR + "/" + y)
        if stat_x.st_ctime < stat_y.st_ctime:
            return -1
        elif stat_x.st_ctime > stat_y.st_ctime:
            return 1
        else:
            return 0


    def file_iterator(file_name, chunk_size=512):

        os.chdir(DIR)
        if file_name == 'latest':
            package_list = os.listdir(DIR)
            package_list.sort(pack_compare)
            file_name = package_list[-1]
        with file(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(app_package))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format("test")
    response['package'] = 'test'
    return response

