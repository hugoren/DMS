#coding:utf-8
import requests
from django.shortcuts import render,render_to_response
import ConfigParser
import argparse

ip = "203.195.140.214"
port = 20000
weight = 10
max_fails = 10
fail_timeout = "10min"
upsteam_zone = "zone_for_backends"
upstream_conf = "../conf/upstream.conf"

upstream_dict = {"a_g_running":["127.0.0.1:30000","127.0.0.1:30001"],\
                 "b_g_running":["127.0.0.1:30002","127.0.0.1:30003"],\
                 "c_g_standy":["127.0.0.1:30004","127.0.0.1:30005"],\
                 "a1_s_running":["127.0.0.1:30000"],"a2_s_running":["127.0.0.1:30001"],\
                 "b1_s_running":["127.0.0.1:30002"],"b2_s_running":["127.0.0.1:30003"],\
                 "c1_s_running":["127.0.0.1:30004"],"c2_s_running":["127.0.0.1:30005"]}


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
        servers_list = r.content
    except Exception as e:
        print e.message
    return render(request,'dtr/lbviews.html',{"upstream_list":servers_list.split(";")})

#list___获取upstream详细的参数信息
def lb_verbose(request):
    url = "http://%s:%s//dynamic?upstream=%s&verbose="%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print  e.message

#update___更新upstream里的servers参数
def lb_update_parameters(request):
    url = "http://%s:%s//dynamic?upstream=%s&server=127.0.0.1:30001&weight=10&max_fails=5&fail_timeout=5"%(ip,port,upsteam_zone)
    try:

        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message

#up___servers_开
def lb_up(upstream_servers):
    if upstream_dict.has_key(upstream_servers):
        for s in upstream_dict[upstream_servers]:
            url = "http://%s:%s//dynamic?upstream=%s&server=%s&up="%(ip,port,upsteam_zone,s)
            try:
                r = requests.get(url)
                print r.content
            except Exception as e:
                print e.message
    else:
        print "%s组或节点不存在"%upstream_servers

#down___servers_关
def lb_down(upstream_servers):
    if upstream_dict.has_key(upstream_servers):
        for s in upstream_dict[upstream_servers]:
            url = "http://%s:%s//dynamic?upstream=%s&server=%s&down="%(ip,port,upsteam_zone,s)
            try:
                r = requests.get(url)
                print r.content
            except Exception as e:
                print e.message
    else:
        print "%s组或节点不存在"%upstream_servers


#add___servers_添加
def lb_add(request):
    url = "http://%s:%s//dynamic?upstream=%s&add=&server=127.0.0.1:30004"%(ip,port,upsteam_zone)
    try:
        r = requests.get(url)
        print r.content
    except Exception as e:
        print e.message


#delete__servers_删除
def lb_remove(request):
    url = "http://%s:%s//dynamic?upstream=%s&remove=&server=%s"%(ip,port,upsteam_zone,"127.0.0.1:30001")
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print "删除成功！"
            print r.content
        elif r.status_code == 400:
            print "该servers不存！"
        else:
            print "删除不成功，请检查其它原因！"

    except Exception as e:
        print e.message


