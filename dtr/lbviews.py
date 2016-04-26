#coding:utf-8
import requests
import request
from django.http import StreamingHttpResponse
from django.shortcuts import  render,render_to_response
from django.http import  HttpResponse
from subprocess import Popen, PIPE, check_output
from argparse import ArgumentParser
import  ConfigParser

class lb():

    # def __init__(self,ip,port,weight,max_fails,fail_timeout,upstream_zone):
    #     self.ip = ip
    #     self.port = port
    #     self.weight = weight
    #     self.max_fails = max_fails
    #     self.fail_timeout = fail_timeout
    #     self.upsteam_zone = upstream_zone

    ip = "203.195.140.214"
    port = 20000
    weight = 10
    max_fails = 10
    fail_timeout = "10min"
    upsteam_zone = "zone_for_backends"
    upstream_conf = "../conf/upstream.conf"


    # 读取配置文件
    def read_conf(object):
        config = ConfigParser.ConfigParser()
        config.read("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf")
        all_config = {}

        for section in config.sections():
            all_config[section] = {}
            for key, value in config.items(section):
                all_config[section][key] = value

        config = all_config["C_standy_servers"]
        print config
        print config["c_standy1"]


    #获取列表
    def lb_list(request):
        url = "http://%s:%s//dynamic?upstream=%s"%(lb.ip,lb.port,lb.upsteam_zone)
        try:
            r = requests.get(url)
            print r.content
        except Exception as e:
            print e.message

    #获取upstream详细的参数信息
    def lb_verbose(request):
        url = "http://%s:%s//dynamic?upstream=%s&verbose="%(lb.ip,lb.port,lb.upsteam_zone)
        try:
            r = requests.get(url)
            print r.content
        except Exception as e:
            print  e.message

    #更新upstream里的servers参数
    def lb_update_parameters(request):
        url = "http://%s:%s//dynamic?upstream=%s&server=127.0.0.1:30001&weight=10&max_fails=5&fail_timeout=5"%(lb.ip,lb.port,lb.upsteam_zone)
        try:
            r = requests.get(url)
            print r.content
        except Exception as e:
            print e.message

    #设置servers_关
    def lb_down(request):
        server_list = ["127.0.0.1:30000","127.0.0.1:30001"]
        for s in server_list:
            url = "http://%s:%s//dynamic?upstream=%s&server=%s&down="%(lb.ip,lb.port,lb.upsteam_zone,s)
            print s
            try:
                r = requests.get(url)
                print r.content
            except Exception as e:
                print e.message


    #设置servers_开
    def lb_up(request):
        server_list = ["127.0.0.1:30000","127.0.0.1:30001"]
        for s in server_list:
            url = "http://%s:%s//dynamic?upstream=%s&server=%s&up="%(lb.ip,lb.port,lb.upsteam_zone,s)
            try:
                r = requests.get(url)
                print r.content
            except Exception as e:
                print e.message

    #设置servers_添加
    def lb_add(request):
        url = "http://%s:%s//dynamic?upstream=%s&add=&server=127.0.0.1:30004"%(lb.ip,lb.port,lb.upsteam_zone)
        try:
            r = requests.get(url)
            print r.content
        except Exception as e:
            print e.message


    #设置servers_删除
    def lb_remove(request):
        url = "http://%s:%s//dynamic?upstream=%s&remove=&server=%s"%(lb.ip,lb.port,lb.upsteam_zone,"127.0.0.1:30001")
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print "删除成功！"
                print r.content
            elif r.status_code == 400:
                print  "该servers不存！"
            else:
                print "删除不成功，请检查其它原因！"

        except Exception as e:
            print e.message

if __name__ == '__main__':

    # lb().lb_list()
    # lb().lb_verbose()
    # lb().lb_update_parameters()
    # lb().lb_down()
    # lb().lb_up()
    # lb().lb_add()
    # lb().lb_remove()
    lb().read_conf()

