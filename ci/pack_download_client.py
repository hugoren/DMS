#coding:utf-8
import  requests
import  sys
import  os



def download_file(parameter_flag,parameter_app,parameter_package,parameter_paakage_save):
    url = 'http://localhost:8000/download_client/?app_flag=%s&app_name=%s&app_package=%s'%(parameter_flag,parameter_app,parameter_package)
    # url = 'http://119.29.104.171:10000/download_client/%s'%parameter_app
    r = requests.get(url)
    os.chdir(parameter_paakage_save)
    if parameter_package == 'latest':
        parameter_package = r.headers['package']
    try:
        with open("%s"%parameter_package,"wb") as pack_content:
            pack_content.write(r.content)
        print "%s,下载成功!"%parameter_package
    except Exception as e:
        return e.message

if __name__ == '__main__':
    parameter_flag = sys.argv[1]
    parameter_app = sys.argv[2]
    parameter_package = sys.argv[3]
    parameter_paakage_save = sys.argv[4]
    download_file(parameter_flag,parameter_app,parameter_package,parameter_paakage_save)




