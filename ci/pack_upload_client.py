#-*-coding:utf-8 -*-

#client端摸拟表单上传
import  urllib2
from  poster.encode import  multipart_encode
from  poster.streaminghttp import register_openers
import  sys
import  os


register_openers()



def upload_file(parameter_app,parameter_version,parameter_package):
    # url = 'http://119.29.104.171:10000/upload/'
    url = 'http://localhost:8000/upload/?app_name=%s&app_version=%s&app_pacakage=%s'%(parameter_app,parameter_version,parameter_package)
    # os.chdir(parameter_path)
    datagen,headers = multipart_encode({"uploadfile":open(parameter_package,'rb')})
    request = urllib2.Request(url,datagen,headers)
    print  urllib2.urlopen(request).read()


if __name__ == '__main__':
    parameter_app = sys.argv[1]
    parameter_version = sys.argv[2]
    parameter_package = sys.argv[3]
    upload_file(parameter_app,parameter_version,parameter_package)
