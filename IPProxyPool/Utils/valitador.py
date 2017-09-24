from requests import Session
from DBmodels.models import proxy as proxyModel
from Utils import DButil
import json
from time import time
from datetime import datetime
import threadpool
req = Session()
def testProxy(ip,port,timeout,scheme=None):
    proxies = { 
            'http': 'http://{ip}:{port}'.format(ip=ip,port=port),           
           }
    try:
        result = req.get('http://119.28.43.115:8088/',proxies=proxies,timeout=timeout)
        result = result.json()
        return result['type']
    except Exception as e :
        print (e)
        return -1

def start_vali(proxy):
    #print ('start vali mark')
    lasttime = time()
    if proxy.scheme == None:
        status = testProxy(proxy.ip,proxy.port,3,'http')
    else:
        status = testProxy(proxy.ip,proxy.port,5,proxy.scheme)
    speed = time() - lasttime
    if status == -1 :#不可用
        if proxy.status == 1:#不可用且状态转换
            proxy.status = 0
            proxy.checkCount = 1
        else:#不可用 不转换状态
            proxy.checkCount += 1
            proxy.status = 0
    else:#可用
        if proxy.status == 1:#可用且状态不转换
            proxy.checkCount += 1
        else:#可用且转换状态
            proxy.status = 1
            proxy.checkCount = 1
        proxy.type = status
        proxy.speed = speed
    print (proxy.ip,proxy.port,proxy.status)
    proxy.lastUpdateTime=datetime.now()
    DButil.DBScopedSession.commit()


def start_vali_process():
    proxyList = DButil.query_all(proxyModel)
    pool = threadpool.ThreadPool(20)  
    requests=[]
    requests.append(threadpool.makeRequests(start_vali,proxyList))
    for req in requests:
        for r in req:
            pool.putRequest(r)
    pool.wait()  