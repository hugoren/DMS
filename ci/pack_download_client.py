import  requests
import  sys

parameter_app = sys.argv[1]
def download_file():
    url = 'http://localhost:8000/download/%s'%parameter_app
    r = requests.get(url)
    with open("%s"%parameter_app,"wb") as code:
        code.write(r.content)
    print  "success"
if __name__ \
        == '__main__':
    download_file()