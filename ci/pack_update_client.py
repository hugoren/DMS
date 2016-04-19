import  requests
import  sys



def update_version(parameter_packageName):
    url = 'http://localhost:8000/update/%s'%(parameter_packageName)
    r = requests.get(url)
    print r.status_code

if __name__ == '__main__':
    parameter_packageName = sys.argv[1]
    # parameter_stable = sys.argv[2]
    update_version(parameter_packageName)