#-*-coding:utf-8 -*-

#client端摸拟表单上传
import  urllib2
from  poster.encode import  multipart_encode
from  poster.streaminghttp import register_openers


register_openers()

parameter_app = sy

def upload_file():
    url = 'http://localhost:8000/upload/'
    datagen,headers = multipart_encode({"uploadfile":open('command_list','rb')})
    request = urllib2.Request(url,datagen,headers)
    print  urllib2.urlopen(request).read()


if __name__ == '__main__':
    upload_file()