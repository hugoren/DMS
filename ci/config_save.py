#coding:utf-8

from ConfigParser import ConfigParser

class read_conf():

    def __init__(self,conf):
        self.conf = conf

    def read_conf(self):
        config = ConfigParser()
        config.read(self.conf)
        all_config = {}

        for section in config.sections():
            all_config[section] = {}
            for key, value in config.items(section):
                all_config[section][key] = value

        config = all_config["save_dir"]
        return config['save_dir']
        # return config['save_dir']

if __name__ == '__main__':
    read_conf('./conf/save_dir.conf').read_conf()
