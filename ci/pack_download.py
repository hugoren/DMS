from django.http import StreamingHttpResponse
from  django.http import  HttpResponse

def pack_download(request):
    # do something...

    def file_iterator(file_name, chunk_size=512):
        with file(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                print "iiii%s"%c
                if c:
                    yield c
                else:
                    break
            # for chunk in f.chunks():
            #     yield  chunk

    the_file_name = '/Users/hugo/PycharmProjects/Dsso/ci/command_list'
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name).

    # return  HttpResponse(response)
    return  response