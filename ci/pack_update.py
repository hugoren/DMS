#conding:utf-8

import  os

def pack_update(request,parameter1,parameter2):
    os.chdir("/Users/hugo/PycharmProjects/Dsso/00")
    os.rename('%s'%parameter1,'%s'%parameter2)

if __name__ == '__main__':
    pack_update()