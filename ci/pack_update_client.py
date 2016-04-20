#coding:utf-8
import  requests
import  sys



def update_version(parameter_packageName):
    # url = 'http://119.29.104.171:10000/update/%s'%(parameter_packageName)
    url = 'http://localost:8000/update/%s'%(parameter_packageName)
    r = requests.get(url)
    if (r.status_code == 200):
        print "%s,包状态更更成功"%parameter_packageName

if __name__ == '__main__':
    parameter_packageName = sys.argv[1]
    # parameter_stable = sys.argv[2]
    update_version(parameter_packageName)
