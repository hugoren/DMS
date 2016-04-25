#coding:utf-8
import requests
import request
from django.http import StreamingHttpResponse
from django.shortcuts import  render,render_to_response
from django.http import  HttpResponse

class lb():

    def __init__(self,ip,port,weight,max_fails,fail_timeout):
        self.ip = ip
        self.port = port
        self.weight = weight
        self.max_fails = max_fails
        self.fail_timeout = fail_timeout

    def view_list(self):
        url = "http://203.195.140.214:20000//dynamic?upstream=zone_for_backends"
        r = requests.get(url)
        print r.content
        return render(request,'dtr/lbviews.html',{'pack_list':r.content})


if __name__ == '__main__':

    lb('203.195.140.214','30000','10','10min','00').view_list()