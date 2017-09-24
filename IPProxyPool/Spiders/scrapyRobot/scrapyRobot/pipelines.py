# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from DBmodels.models import proxy,webPage
from Utils import DButil
from collections import defaultdict
from urllib.parse import urlparse

class ProxySpiderPipeline(object):
    url_set=set()
    def process_item(self, item, spider):
        netloc=urlparse(item['source']).netloc
        webPageItem = DButil.session.query(webPage).filter(webPage.webUrl==netloc).first()
        if not item['source'] in self.url_set:
            self.url_set.add(item['source'])
            webPageItem.subPageCount += 1
        webPageItem.proxyCount += 1
        proxyItem = proxy()
        proxyItem.ip = item['ip']
        proxyItem.port = item['port']
        proxyItem.createTime = item['createTime']
        proxyItem.lastUpdateTime = item['createTime']
        proxyItem.source = netloc
        DButil.add(proxyItem)
        DButil.commit()
        return item
