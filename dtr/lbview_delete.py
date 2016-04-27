#coding:utf-8
import requests
from django.shortcuts import render,render_to_response

ip = "203.195.140.214"
port = 20000
weight = 10
max_fails = 10
fail_timeout = "10min"
upsteam_zone = "zone_for_backends"


def lb_delete(request):

    if request.method == 'POST':
        delete_server = request.POST.get('upstream_server')
        print delete_server.split(" ")[-1]
        try:
            # url = "http://%s:%s//dynamic?upstream=%s&remove=&server=%s"%(ip,port,upsteam_zone,delete_server)
            url = "http://%s:%s/dynamic?upstream=%s&remove=&server=%s"%(ip,port,upsteam_zone,delete_server.split(" ")[-1])
            print url
            r = requests.get(url)
            print r.content
            return render(request,'dtr/lbviews.html')
        except Exception as e:
            print e.message