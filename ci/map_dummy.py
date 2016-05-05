#coding:utf-8
import urllib2
import requests
from multiprocessing.dummy import Pool as ThreadPool
def map_dummy(functions,squeue):
    # urls = [
    #   'http://www.python.org',
    #   'http://www.python.org/about/',
    #   'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    #   'http://www.python.org/doc/',
    #   'http://www.python.org/download/',
    #   'http://www.python.org/getit/',
    #   'http://www.python.org/community/',
    #   'https://wiki.python.org/moin/',
    #   'http://planet.python.org/',
    #   'https://wiki.python.org/moin/LocalUserGroups',
    #   'http://www.python.org/psf/',
    #   'http://docs.python.org/devguide/',
    #   'http://www.python.org/community/awards/'
    #   ]

    # 创建一个工作者线程池
    pool = ThreadPool(4)
    # 在各个线程中打开url，并返回结果
    results = pool.map(functions,squeue)
    #close the pool and wait for the work to finish
    # 关闭线程池，等待工作结束
    pool.close()
    pool.join()
    return results
if __name__ == '__main__':
    map_dummy()