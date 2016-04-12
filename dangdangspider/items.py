# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # 书名
    title = scrapy.Field()

    # 作者 
    author = scrapy.Field()

    # 出版社 
    publisher = scrapy.Field()

    # 出版时间 
    ptime = scrapy.Field()

    # 排名 
    #ranking = scrapy.Field()

    # 评论数 
    commentnum = scrapy.Field()

    # 价格名称（当当价或者尾品价）
    pricename = scrapy.Field()

    # 具体价格 
    price = scrapy.Field()

    #URL
    url = scrapy.Field()
    pass
