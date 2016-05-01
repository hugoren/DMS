#-*-coding:utf-8 -*-

#client端摸拟表单上传
import urllib2
from poster.encode import  multipart_encode
from poster.streaminghttp import register_openers
import sys
import  os
import requests

register_openers()


#模拟表单，流式上传
def upload_file(parameter_app,parameter_version,parameter_package):
    # url = 'http://119.29.104.171:10000/upload/'
    # url = 'http://119.29.104.171:10000/upload/?app_name=%s&app_version=%s&app_package=%s'%(parameter_app,parameter_version,parameter_package)
    # os.chdir(parameter_path)
    url = 'http://localhost:8000/upload/?app_name=%s&app_version=%s&app_package=%s'%(parameter_app,parameter_version,parameter_package)
    datagen,headers = multipart_encode({"uploadfile":open(parameter_package,'rb')})
    request = urllib2.Request(url,datagen,headers)
    print urllib2.urlopen(request).read()


#包状态变更
def update_version(parameter_app,parameter_package):
    # url = 'http://119.29.104.171:10000/update/%s'%(parameter_packageName)
    #django传参一种方式
    # url = 'http://localhost:8000/update/%s'%(parameter_packageName)
    url = 'http://localhost:8000/update/?app_name=%s&app_package=%s'%(parameter_app,parameter_package)
    # url = 'http://119.29.104.171:10000/update/?app_name=%s&app_package=%s'%(parameter_app,parameter_package)

    r = requests.get(url)
    if (r.status_code == 200):
        print "%s,包状态更更成功"%parameter_package

#包下载
def download_file(parameter_flag,parameter_app,parameter_package,parameter_paakage_save):
    url = 'http://localhost:8000/download_client/?app_flag=%s&app_name=%s&app_package=%s'%(parameter_flag,parameter_app,parameter_package)
    # url = 'http://119.29.104.171:10000/download_client/?app_flag=%s&app_name=%s&app_package=%s'%(parameter_flag,parameter_app,parameter_package)
    r = requests.get(url)
    os.chdir(parameter_paakage_save)
    #把latest转换成最新的包名
    if parameter_package == 'latest':
        parameter_package = r.headers['package']
    try:
        with open("%s"%parameter_package,"wb") as pack_content:
            pack_content.write(r.content)
        print "%s,下载成功!"%parameter_package
        sys.exit(0)
    except Exception as e:
        return e.message


if __name__ == '__main__':
    parameter_flag = sys.argv[1]
    parameter_app = sys.argv[2]
    parameter_package = sys.argv[3]
    parameter_paakage_save = sys.argv[4]
    download_file(parameter_flag,parameter_app,parameter_package,parameter_paakage_save)






#包状态更新
if __name__ == '__main__':
    parameter_app = sys.argv[1]
    parameter_package = sys.argv[2]
    update_version(parameter_app,parameter_package)



#包下载
if __name__ == '__main__':
    parameter_app = sys.argv[1]
    parameter_version = sys.argv[2]
    parameter_package = sys.argv[3]
    upload_file(parameter_app,parameter_version,parameter_package)
