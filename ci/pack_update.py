#coding:utf-8
import os
import time
import shutil
import datetime
from  django.http import  HttpResponse

def pack_update(request,parameter1,parameter2):

    # format = '%Y-%m-%d-%H:%M:%S'
    # value = time.localtime(time.time())
    # value = time.localtime()
    # dt = time.strftime(format, value)
    a = datetime.datetime.today()
    o = datetime.timedelta(hours=8)
    # print (a+o).strftime("%Y-%m-%d_%H:%M")
    # dt = time.strftime("%Y-%m-%d_%H-%M",time.localtime(time.time()))
    filename_list = str(parameter1).split('_')
    pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
    os.chdir(pack_path)
    if not os.path.exists(filename_list[0]):
        os.makedirs(filename_list[0])
    os.chdir(pack_path+'/'+filename_list[0])
    if not os.path.exists(filename_list[1]):
        os.makedirs(filename_list[1])
    os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1])
    if not os.path.exists("stable"):
            os.makedirs("stable")
    os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+filename_list[2])
    try:
        print  parameter1
        shutil.copy2(parameter1,pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+"stable")
        os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+parameter2)
        # os.renames(parameter1,"%s_%s_.tar.gz"%(filename_list[0],filename_list[1])
        # os.renames('06.tar.gz','07.tar.gz')
        os.renames(parameter1,"%s_%s_%s_%s.tar.gz"%(filename_list[0],filename_list[1],parameter2,(a+o).strftime("%Y-%m-%d_%H:%M")))
    except Exception as e:
        return e.message
    return HttpResponse(u'{}变更成功%s'.format(parameter1))


if __name__ == '__main__':
    pack_update()