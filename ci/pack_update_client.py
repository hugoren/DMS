#coding:utf-8
import  requests
import  sys



def update_version(parameter_app,parameter_package):
    # url = 'http://119.29.104.171:10000/update/%s'%(parameter_packageName)
    #django传参一种方式
    # url = 'http://localhost:8000/update/%s'%(parameter_packageName)
    url = 'http://localhost:8000/update/?app_name=%s&app_package=%s'%(parameter_app,parameter_package)
    r = requests.get(url)
    if (r.status_code == 200):
        print "%s,包状态更更成功"%parameter_package

if __name__ == '__main__':
    parameter_app = sys.argv[1]
    parameter_package = sys.argv[2]
    update_version(parameter_app,parameter_package)
