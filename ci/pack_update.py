#coding:utf-8
import os
import shutil
from  django.http import  HttpResponse
import config_save

def pack_update(request):


    app_name = request.GET.get('app_name','')
    app_package = request.GET.get('app_package','')

    pack_path = config_save.read_public_conf().read_repository()
    first_layer = 'release'
    os.chdir(pack_path)
    if not os.path.exists(first_layer):
        os.makedirs(first_layer)
    os.chdir(pack_path+'/'+first_layer)
    if not os.path.exists(app_name):
        os.makedirs(app_name)
    os.chdir(pack_path+'/'+'snapshot'+'/'+app_name)
    try:
        shutil.copy2(app_package,pack_path+'/'+first_layer+'/'+app_name)
        # os.chdir(pack_path+'/'+dir_update+'/'+app_name)
        # os.renames(parameter1,"%s_%s_%s_%s.tgz"%(filename_list[0],filename_list[1],'release',(a+o).strftime("%Y%m%d%H%M")))
    except Exception as e:
        return e.message
    return HttpResponse(u'{}变更成功%s'.format(app_package))


if __name__ == '__main__':
    pack_update()