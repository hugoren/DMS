#coding:utf-8'

from django.http import StreamingHttpResponse
import os
import config_save
import map_dummy

def pack_download(request):

    app_flag = request.GET.get('app_flag','')
    app_name = request.GET.get('app_name','')
    app_package = request.GET.get('app_package','')
    pack_path = config_save.read_public_conf().read_repository("repository_dir","repository")
    DIR = pack_path+'/'+app_flag+'/'+app_name
    global pack_name

    def pack_compare(x, y):
        stat_x = os.stat(DIR + "/" + x)
        stat_y = os.stat(DIR + "/" + y)
        if stat_x.st_ctime < stat_y.st_ctime:
            return -1
        elif stat_x.st_ctime > stat_y.st_ctime:
            return 1
        else:
            return 0
    if app_package == 'latest':
        p_list = os.listdir(DIR)
        p_list.sort(pack_compare)
        global p_name
        p_name = p_list[-1]

    def file_iterator(file_name, chunk_size=512):
        os.chdir(DIR)

        if file_name == 'latest':
            file_name = p_name
        with file(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break


    #调用file_iterator方法，流式下载包
    # response = StreamingHttpResponse(file_iterator(app_package))
    response = StreamingHttpResponse(map_dummy.map_dummy(file_iterator,app_package))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format("test")
    if app_package == 'latest':
        print p_name
        response['package'] = p_name
    return response

