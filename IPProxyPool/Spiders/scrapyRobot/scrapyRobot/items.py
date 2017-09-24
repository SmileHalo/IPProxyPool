# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxySpiderItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    createTime = scrapy.Field()
    source = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
