import  requests
import  sys

parameter_snapshot = sys.argv[1]
parameter_stable = sys.argv[2]

def update_version():
    url = 'http://localhost:8000/update/%s/%s'%(parameter_snapshot,parameter_stable)
    print parameter_snapshot
    r = requests.get(url)
    print r.status_code

if __name__ == '__main__':
    update_version()