#-*-conding:utf-8-*-

import redis

class pyRedis:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = '6379'
        self.db = 0
        # self.c = redis.StrictRedis(host=self.host,port=self.port,db=self.db)
        pool = redis.ConnectionPool(host=self.host,port=self.port,db=self.db)
        self.r = redis.Redis(connection_pool=pool)
        # self.c = redis.Redis(host=self.host,port=self.port,db=self.db)


    def set_key(self,key,valuse):
        try:
            return  self.r.set(key,valuse)
        except Exception as e:
            print  e.message

    def get_key(self,key):
        try:
            return self.r.get(key)
        except Exception as e:
            print  e.message

# pyRedis().set_key("00","01")
# print  pyRedis().get_key("00")
