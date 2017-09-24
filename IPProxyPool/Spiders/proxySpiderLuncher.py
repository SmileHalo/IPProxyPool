# -*- coding: utf-8 -*-
import scrapy
from Utils import DButil
from scrapy.crawler import CrawlerProcess
from DBmodels.models import webPage
#from scrapy.utils.project import get_project_settings
from Spiders.scrapyRobot.scrapyRobot import settings
from Spiders.scrapyRobot.scrapyRobot.spiders.proxySpider import proxySpider

def start_crawl_process():
    #settings = get_project_settings()
    st={}
    for k,v in settings.__dict__.items():
        if k[:2]!='__':
            st[k]=v
    process = CrawlerProcess(st)
    process.crawl(proxySpider)
    process.start() # the script will block here until all crawling jobs are finished

#class ProxyspiderSpider(scrapy.Spider):
#    name = "proxySpider"
#    allowed_domains = []
#    webPageList = DButil.query_all(webPage)
#    urls = []
#    for i in webPageList:
#        urls.append(i.scheme + '://' + i.webUrl)
#    start_urls = urls
#   # allowed_domains = urls
#    def parse(self, response):
#        print(response)