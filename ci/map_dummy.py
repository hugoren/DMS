#coding:utf-8
import urllib2
import requests
from multiprocessing.dummy import Pool as ThreadPool
def map_dummy(functions,squeue):

    # 创建一个工作者线程池
    pool = ThreadPool(4)
    # 在各个线程中打开url，并返回结果
    results = pool.map(functions,squeue)
    # 关闭线程池，等待工作结束
    pool.close()
    pool.join()
    return results
if __name__ == '__main__':
    map_dummy()