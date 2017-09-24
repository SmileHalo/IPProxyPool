from requests import Session
from urllib.parse import urlparse
from DBmodels.models import webPage
from datetime import datetime
from Utils import DButil
req = Session()
req.headers['Ocp-Apim-Subscription-Key']='3026f293ca564106a5ba197df5ac0c7a'
req.headers['User-Agent']='Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822)'

def json_to_dbmodels(jsonData):
    ret = []
    urlSet=set()
    for i in jsonData['webPages']['value']:
        if (not i['displayUrl'].startswith('http')):
            i['displayUrl'] = 'http://'+i['displayUrl']
        model=webPage()
        tmpUrl = i['displayUrl']
        if (not tmpUrl.startswith('http')):
            tmpUrl = 'http://'+tmpUrl
        
        if urlparse(tmpUrl).netloc=='':
            model.webUrl=tmpUrl
        else:
            model.webUrl=urlparse(tmpUrl).netloc
        if urlparse(tmpUrl).scheme != 'http':
            model.scheme = 'https'
        else :
            model.scheme = 'http'
        model.webName=i['name']
        model.updateTime=datetime.now()
        if (model.webUrl in urlSet):
            continue
        urlSet.add(model.webUrl)
        ret.append(model)
    return ret
def get_webpages_bing(keyword):
    baseurl = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    params={ 'q':keyword,
            'mkt':'zh-cn',
            'count':50,
            'responseFilter':'Webpages',
            }
    result = req.get(baseurl,params=params).json()
    return json_to_dbmodels(result)

def start_crawl():
    #webPages = get_webpages_bing('免费代理IP')
    webPages = get_webpages_bing('http代理IP')
    for i in webPages:
        DButil.merge(i)
    webPages = set(webPages)
    #DButil.add_all(webPages)
    DButil.commit()
    pass
#a=req.get(r'https://api.cognitive.microsoft.com/bing/v5.0/search?q=sailing+lessons+seattle&mkt=en-us')
#print(a)
#pass



'''
GET https://api.cognitive.microsoft.com/bing/v5.0/search?q=sailing+lessons+seattle&mkt=en-us HTTP/1.1  
Ocp-Apim-Subscription-Key: 123456789ABCDE  
User-Agent: Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822)  
X-Search-ClientIP: 999.999.999.999  
X-Search-Location: lat:47.60357;long:-122.3295;re:100  
X-MSEdge-ClientID: <blobFromPriorResponseGoesHere>  
Host: api.cognitive.microsoft.com  
'''