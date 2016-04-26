 #coding:utf-8
import  ConfigParser

 # 读取配置文件
def read_conf():
    config = ConfigParser.ConfigParser()
    config.read("/Users/hugo/PycharmProjects/Dsso/dtr/conf/upstream.conf")
    all_config = {}
    # age = config.get("1","2")
    # print age
    print  config.sections()
    for section in config.sections():
        all_config[section] = {}
        for key, value in config.items(section):
            all_config[section][key] = value

        # config = all_config["C_standy_servers"]
        # print config["C_standy_servers"]
    print config.sections()

read_conf()