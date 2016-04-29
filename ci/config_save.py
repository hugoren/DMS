#coding:utf-8

from ConfigParser import ConfigParser

class read_public_conf(object):

    # def __init__(self,conf):
    #     self.conf = conf

    def read_repository(self):
        repository_conf = '/Users/hugo/PycharmProjects/Dsso/ci/conf/save_dir.conf'
        config = ConfigParser()
        config.read(repository_conf)
        all_config = {}

        for section in config.sections():
            all_config[section] = {}
            for key, value in config.items(section):
                all_config[section][key] = value

        #根据两层取值，先取[],再取相应的key
        config = all_config["repository_dir"]
        return config["repository"]

if __name__ == '__main__':
   read_public_conf().read_repository()