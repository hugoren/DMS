import  requests
import  sys

parameter_app = sys.argv[1]
def download_file():
    url = 'http://localhost:8000/download'
    r = requests.get(url)
    with open("%s.tar.gz"%parameter_app,"wb") as code:
        code.write(r.content)
    print  "success"
if __name__ == '__main__':
    download_file()