#coding:utf-8
import  requests
import  sys
import  os

#存储路径
download_dir = sys.argv[1]
#下载包名称
parameter_app = sys.argv[2]

def download_file():
    url = 'http://localhost:8000/download_client/%s'%parameter_app
    r = requests.get(url)
    os.chdir(download_dir)
    try:
        with open("%s"%parameter_app,"wb") as pack_content:
            pack_content.write(r.content)
        print "下载成功!"
    except Exception as e:
        return e.message

if __name__ == '__main__':
    download_file()




