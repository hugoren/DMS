#coding:utf-8
import requests
import request
from django.http import StreamingHttpResponse
from django.shortcuts import  render,render_to_response
from django.http import  HttpResponse
from subprocess import Popen, PIPE, check_output
import ConfigParser
import argparse
import  sys

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

upstream_dict = {"A_running":["127.0.0.1:30000","127.0.0.1:30001"],"B_running":["127.0.0.1:30000","127.0.0.1:30001"],"C_standy":'["127.0.0.1:300,04","127.0.0.1:30005"]'}
B_running = ["1270.0.1:30002","127.0.0.1:30003"]
C_standy = ["127.0.0.1:300,04","127.0.0.1:30005"]

# 读取配置文件
def read_conf():
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

# 读取调用参数
def read_argparse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-s", "--server", dest="ACTION", action='store', default='', help="启动/停止/重启应用.")
    group.add_argument("-p", "--publish", dest="VERSION", action='store', default='', help="发布/回滚应用.")
    parser.add_argument("-b", "--backup", action='store_true', help="发布前进行否备份.")
    parser.add_argument("app", action='store', help="应用名称.")

    given_args = parser.parse_args()

    return given_args


#获取列表
def lb_list(request):
    url = "http://%s:%s//dynamic?upstream=%s"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
        # return render(request,'dtr/lbviews.html')
    except Exception as e:
        print e.message

#获取upstream详细的参数信息
def lb_verbose(request):
    url = "http://%s:%s//dynamic?upstream=%s&verbose="%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print  e.message

#更新upstream里的servers参数
def lb_update_parameters(request):
    url = "http://%s:%s//dynamic?upstream=%s&server=127.0.0.1:30001&weight=10&max_fails=5&fail_timeout=5"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message

#设置servers_关
def lb_down(upstream_servers):
    # server_list = ["127.0.0.1:30000","127.0.0.1:30001"]
    # A_running = ["127.0.0.1:30000","127.0.0.1:30001"]
    server_list = upstream_dict[upstream_servers]
    for s in server_list:
        # url = "http://%s:%s//dynamic?upstream=%s&server=%s&down="%(ip,port,upsteam_zone,s)
        # print s
        try:
            # r = requests.get(url)
            # print r.content
            print s
        except Exception as e:
            print e.message


#设置servers_开
def lb_up(request,upstream_list):
    # server_list = ["127.0.0.1:30000","127.0.0.1:30001"]
    for s in upstream_list:
        url = "http://%s:%s//dynamic?upstream=%s&server=%s&up="%(ip,port,upsteam_zone,s)
        try:
            r = requests.get(url)
            print r.content
        except Exception as e:
            print e.message

#设置servers_添加
def lb_add(request):
    url = "http://%s:%s//dynamic?upstream=%s&add=&server=127.0.0.1:30004"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message


#设置servers_删除
def lb_remove(request):
    url = "http://%s:%s//dynamic?upstream=%s&remove=&server=%s"%(ip,port,upsteam_zone,"127.0.0.1:30001")
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
def lb_list():
    url = "http://%s:%s//dynamic?upstream=%s"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
        # return render(request,'dtr/lbviews.html')
    except Exception as e:
        print e.message

#获取upstream详细的参数信息
def lb_verbose():
    url = "http://%s:%s//dynamic?upstream=%s&verbose="%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print  e.message

#更新upstream里的servers参数
def lb_update_parameters():
    url = "http://%s:%s//dynamic?upstream=%s&server=127.0.0.1:30001&weight=10&max_fails=5&fail_timeout=5"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message

#设置servers_关
def lb_down(server_key):
    # A_running = ["127.0.0.1:30000","127.0.0.1:30001"]
    server_list = upstream_dict[server_key]
    for s in server_list:
        # url = "http://%s:%s//dynamic?upstream=%s&server=%s&down="%(ip,port,upsteam_zone,s)
        try:
            # r = requests.get(url)
            # print r.content
            print  s
        except Exception as e:
            print e.message


#设置servers_开
def lb_up(request):
    server_list = ["127.0.0.1:30000","127.0.0.1:30001"]
    for s in server_list:
        url = "http://%s:%s//dynamic?upstream=%s&server=%s&up="%(ip,port,upsteam_zone,s)
        try:
            r = requests.get(url)
            print r.content
        except Exception as e:
            print e.message

#设置servers_添加
def lb_add():
    url = "http://%s:%s//dynamic?upstream=%s&add=&server=127.0.0.1:30004"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message


#设置servers_删除
def lb_remove():
    url = "http://%s:%s//dynamic?upstream=%s&remove=&server=%s"%(ip,port,upsteam_zone,"127.0.0.1:30001")
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

    # lb_list()
    # lb_verbose()
    # lb().lb_update_parameters()
    # lb().lb_down()
    # lb().lb_up()
    # lb().lb_add()
    # lb().lb_remove()
    # lb().read_conf()
    # lb().argparse()
    # args = argparse()
    # up = args.app
    actions = sys.argv[1]
    if actions == 'list':
        lb_list()

    elif actions == 'down':
        lb_down(sys.argv[2])

    elif actions == 'up':
        lb_up(request)
    # args = read_argparse()
    # actions = args.app
    # print actions
    # print '%s()'%actions
    # actions()