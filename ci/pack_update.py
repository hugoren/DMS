#coding:utf-8
import os
import shutil
import datetime
from  django.http import  HttpResponse

def pack_update(request,parameter1):

    #由于python默认是utf,这里＋8
    a = datetime.datetime.today()
    o = datetime.timedelta(hours=8)

    filename_list = str(parameter1).split('_')
    pack_path = '/Users/hugo/PycharmProjects/Dsso/00'
    os.chdir(pack_path)
    if not os.path.exists(filename_list[0]):
        os.makedirs(filename_list[0])
    os.chdir(pack_path+'/'+filename_list[0])
    if not os.path.exists(filename_list[1]):
        os.makedirs(filename_list[1])
    os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1])
    if not os.path.exists("release"):
            os.makedirs("release")
    os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+filename_list[2])
    try:
        shutil.copy2(parameter1,pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+"release")
        os.chdir(pack_path+'/'+filename_list[0]+'/'+filename_list[1]+'/'+'release')
        # os.renames(parameter1,"%s_%s_.tar.gz"%(filename_list[0],filename_list[1])
        # os.renames('06.tar.gz','07.tar.gz')
        os.renames(parameter1,"%s_%s_%s_%s.tgz"%(filename_list[0],filename_list[1],'release',(a+o).strftime("%Y%m%d%H%M")))
    except Exception as e:
        return e.message
    return HttpResponse(u'{}变更成功%s'.format(parameter1))


if __name__ == '__main__':
    pack_update()