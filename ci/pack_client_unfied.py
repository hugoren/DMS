#-*-coding:utf-8 -*-

import urllib2
from poster.encode import  multipart_encode
from poster.streaminghttp import register_openers
import sys
import os
import requests
import argparse

#读取命令行参数
def read_argparse():
    parser = argparse.ArgumentParser(description="读取包状态变更的命令行参数")
    group = parser.add_argument_group()
    group.add_argument('upload',help="上传包",action='store_true')
    group.add_argument('update',help='包状包变更',action='store')
    group.add_argument('download',help='包下载',action='store')
    given_args = parser.parse_args()
    return given_args



#模拟表单，流式上传
register_openers()
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


#
# #包上传
# if __name__ == '__main__':
#     parameter_flag = sys.argv[1]
#     parameter_app = sys.argv[2]
#     parameter_package = sys.argv[3]
#     parameter_paakage_save = sys.argv[4]
#     download_file(parameter_flag,parameter_app,parameter_package,parameter_paakage_save)
#
#
# #包状态更新
# if __name__ == '__main__':
#     parameter_app = sys.argv[1]
#     parameter_package = sys.argv[2]
#     update_version(parameter_app,parameter_package)
#
#
#
# #包下载
# if __name__ == '__main__':
#     parameter_app = sys.argv[1]
#     parameter_version = sys.argv[2]
#     parameter_package = sys.argv[3]
#     upload_file(parameter_app,parameter_version,parameter_package)


#读取命令行参数
if __name__ == '__main__':
    given_args = read_argparse()
    app = given_args.app
    version = given_args.version
    publish = given_args.publish
    print '%s_%s_%s'%(app,version,publish)

