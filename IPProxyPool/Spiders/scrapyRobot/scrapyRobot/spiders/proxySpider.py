# -*- coding: utf-8 -*-
import scrapy
from Utils import DButil
from DBmodels.models import webPage
from Spiders.scrapyRobot.scrapyRobot.items import ProxySpiderItem
import re
from datetime import datetime
from urllib.parse import urljoin,urlparse
from requests import Session
from ezfile import write_out
req = Session()
req.headers['User-Agent']='Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822)'

class proxySpider(scrapy.Spider):
    name = "proxySpider"
    #allowed_domains = []
    webPageList = DButil.query_all(webPage)
    urls = []
    for i in webPageList:
        urls.append(i.scheme + '://' + i.webUrl)
    start_urls = urls
    #start_urls = [r'http://www.goubanjia.com/free/index.shtml']
    #start_urls = [r'http://www.mayidaili.com/']
   # start_urls = [r'http://www.goubanjia.com/']
    
    re_rule=re.compile(r"((?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]))[\s:]+(6[0-5]{2}[0-3][0-5]|[1-5]\d{4}|[1-9]\d{1,3}|[0-9])")
    # (IP port)或者(IP:port)

    def parse(self,response):
        ## 如果不存在图片信息
        webText = response.meta['textContent']
        proxyList = self.re_rule.findall(webText)
        for item in proxyList:
            ip,port=item
            source = response.url
            yield ProxySpiderItem(ip=ip,port=port,source=source,createTime=datetime.now())

    #def parse1(self, response):
    #   # print(response)
    #    ipList = re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',response.text)
    #    if len(ipList) > 0:
    #        for ip in ipList:
    #            portTag = response.xpath('//td[text()="{IP}"]/following-sibling::td'.format(IP=ip))[0].extract()
    #            port = re.sub('<.+?>','',portTag)
    #            source = response.url
    #            if port != "" or port == None:
    #                yield ProxySpiderItem(ip=ip,port=port,source=source,createTime=datetime.now())
    #            else :
    #                pass
    #                #todo: 仅有地址 端口做了反爬处理

    #            #imgUrl = re.findall(r'<img.+?src="(.+?)"',portTag) #还可能有数据绑定标签
    #            #try:
    #            #    if not urlparse(imgUrl).netloc:
    #            #        imgUrl=urljoin(response.url,imgUrl)
    #            #except:
    #            #    pass
    #            #    #todo: IMG图片路径特殊无法解析
    #            #portImage = req.get(imgUrl).content
    #            #write_out('1.gif',portImage)
    #            #pass
    #    pass