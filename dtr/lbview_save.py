#coding:utf-8
import requests

ip = "203.195.140.214"
port = 20000
weight = 10
ip = "203.195.140.214"
port = 20000
weight = 10
max_fails = 10
fail_timeout = "10min"
upsteam_zone = "zone_for_backends"
upstream_conf = "../conf/upstream.conf"

def lb_save():
    url = "http://%s:%s//dynamic?upstream=%s&server=127.0.0.1:30001&weight=10&max_fails=5&fail_timeout=5"%(ip,port,upsteam_zone)
    try:

        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message