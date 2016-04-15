#-*-coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from  django import  forms
from  django.http import  HttpResponse
import  os
import  requests
import request
import  dict
import  chunk
import  time
import  urllib2
from  poster.encode import  multipart_encode
from  poster.streaminghttp import register_openers
# def upFile(f):
#     upload_dir = '/Users/hugo/PycharmProjects/Dsso/ci/upload'
#     #
#     # file_name = "command_list"
#
#     try:
#         path = "./00"
#         if not os.path.exists(path):
#             os.makedirs(path)
#             f = "command_list"
#             destination = open('./command_list', 'wb+')
#             for chunk in f.chunks():
#                 destination.write(chunk)
#             destination.close()
#     except Exception, e:
#         print e
#
#     return f
#     f.close()
#
# # upFile("command_list")
#
# def upload_api():
#     url = 'http://localhost:8000/post'
#     files = {'file':open('command_list','rb')}
#     r = requests.post(url,files=files)
#     r.cookies['test']
#     print  r.text
#
#
# def read_file(filename, buf_size=8192):
#   with open(filename, "rb") as f:
#         while True:
#             content = f.read(buf_size)
#             if content:
#                  yield content
#             else:
#                 break
#
# def big_file_download(request):
#   filename = "commad_list"
#   response = HttpResponse(read_file(filename))
#   return response
register_openers()

def upload_file():
    url = 'http://localhost:8000/upload/'
    # files = {'file':open('command_list','rb')}
    # r = requests.post(url,files=files)
    # print  r.status_code
    # with open('command_list','rb') as f:
    #     r = requests.post(url,data=f)
    #     print  f
    #     print r.status_code
    datagen,headers = multipart_encode({"uploadfile":open('command_list','rb')})
    request = urllib2.Request(url,datagen,headers)
    print  urllib2.urlopen(request).read()
upload_file()