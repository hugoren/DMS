#coding:utf-8'

#web方式下载
from django.http import StreamingHttpResponse
from  django.http import  HttpResponse

#web版下载
def pack_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with file(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = '/Users/hugo/PycharmProjects/Dsso/00/admin-1.0-SNAPSHOT.tgz20160329-094622'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    # return  HttpResponse(response)
    return  response

