#conding:utf-8

import  os

def pack_update():
    os.chdir("/Users/hugo/PycharmProjects/Dsso/00")
    os.rename('t1','t2')

if __name__ == '__main__':
    pack_update()