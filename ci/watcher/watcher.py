#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from ConfigParser import ConfigParser
from datetime import datetime, timedelta
import urllib2
import json
import os


# 读取配置
def read_conf(app, conf="/Users/xufei/PycharmProjects/frigate/frigate-watcher/watcher/watcher.conf"):
    config = ConfigParser()
    config.read(conf)
    all_config = {}

    for section in config.sections():
        all_config[section] = {}
        for key, value in config.items(section):
            all_config[section][key] = value

    needed_config = {}
    needed_config['es'] = all_config["default"]["elasticsearch"]
    needed_config['grahite'] = all_config["default"]['grahite']

    check_list = all_config["default"][app]
    needed_config['check_list']=check_list.split(",")


    # 获取检查项的阀值
    needed_config['checks'] = {}
    for check in needed_config['check_list']:
        needed_config['checks'][check] = all_config[check]

    return needed_config


# 用户http请求
def url_request(url, data = None):
    """用于实现http请求,接受url和要上传的数据字典,返回json格式的数据"""

    if data is None:
        response = urllib2.urlopen(url)
    else:
        data = json.dumps(data)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)

    return json.loads(response.read())


# 获取5分钟内的错误日志数
def get_error_count(es_addr, index, node):
    url = "http://%s/%s/_count?pretty=1" % (es_addr, index)
    a = datetime.utcnow() - timedelta(seconds=300)
    date = a.strftime('%Y-%m-%dT%H:%M:%S')

    values = {
                "query": {
                    "bool": {
                        "must": [
                            {
                                "range": {
                                    "@timestamp": {
                                        "gte": date
                                    }
                                }
                            },
                            {
                                "term": {
                                    "type": node
                                }
                            }
                        ]
                    }
                }
                }
    result = url_request(url, values)
    return result["count"]


# 通过grahite获取kamon监测数据
def get_grahite_data(target, host):
    url = "http://%s/render/?&target=%s&from=-30s&format=json&integral" % (host, target)
    result = url_request(url)
    sum = 0
    count = 0
    for item in result[0]["datapoints"]:
        if item[0] is not None:
            if "Third-Weixin-custom-send" in target:
                sum += item[0]/1000000
            else:
                sum += item[0]
            count += 1
    return int(sum/count)



# 通过配置文件设定的阀值,判断检测项状态
def get_status(checks, check_result):
    status = {}
    for key in checks.keys():
        error = checks[key]["error"]
        warning = checks[key]["warning"]

        if key == "doctor_conn":
            if int(check_result[key]) >int(warning):
                status[key] = "ok"
            elif int(check_result[key]) < int(error):
                status[key] = "error"
            else:
                status[key] = "warning"
        else:
            if int(check_result[key]) < int(warning):
                status[key] = "ok"
            elif int(check_result[key]) > int(error):
                status[key] = "error"
            else:
                status[key] = "ok"

    if "error" in status.values():
        status["status"] = "error"
    elif "warning" in status.values():
        status["status"] = "warning"
    else:
        status["status"] = "ok"
    return status


# 获取应用健康状态
def health(app, node):
    """传入app名称和节点名称,可以从log和apm系统获取相应健康数据"""
    conf_file = "/Users/xufei/PycharmProjects/frigate/frigate-watcher/watcher.conf"
    data = {}
    data["app"] = app
    data["node"] = node
    check_result = {}

    if not os.path.isfile(conf_file):
        data["status"] = "failed"
        data["message"] = "config file not exist."
        return json.dumps(data, indent=4)

    try:
        config = read_conf(app, conf=conf_file)
        grahite = config["grahite"]
        es = config["es"]
    except KeyError:
        data["status"] = "failed"
        data["message"] = "app not exist."
        return json.dumps(data, indent=4)

    try:
        for check in config['check_list']:
            if check == "error_count":
                error_count = get_error_count(es, "%s_info" % app, node)
                check_result[check] = error_count
            else:
                target = config['checks'][check]["target"]
                result = get_grahite_data("stats.timers.%s.%s.%s" % (app, node, target), grahite)
                check_result[check] = result

        status = get_status(config["checks"], check_result)
        data['details'] = {}
        for key in  check_result.keys():
            data['details'][key] = {}
            data['details'][key]["result"] = check_result[key]
            data['details'][key]["status"] = status[key]

        data["status"] = status["status"]
    except Exception, error:
        data["status"] = "failed"
        data["message"] = "%s" % error

    return json.dumps(data, indent=4)


if __name__ == "__main__":
    print health("mobile", "mobile3")
