#!/usr/bin/env python
# coding=utf-8

import scrapy
from scrapy.selector import Selector
from dangdangspider.items import DangdangspiderItem 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

class DangdangSpider(CrawlSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = [#'http://category.dangdang.com/cp01.54.04.03.00.00.html', #linux
                  #'http://category.dangdang.com/cp01.54.06.06.00.00.html',  #java
                  #'http://category.dangdang.com/cp01.54.10.00.00.00.html',  #计算机理论
                  #'http://category.dangdang.com/cp01.54.11.00.00.00.html',  #行业软件及应用
                  'http://category.dangdang.com/cp01.54.12.00.00.00.html',  #人工智能
                 ]

    
    rules = [
        #Rule(sle(allow=("/pg\d-cp01.54", )), follow=True),

        #Rule(sle(allow=("product.dangdang.com/\d+\.html#ddclick\?")), callback='parse_item'),
        Rule(sle(allow=("product.dangdang.com/23898620\.html#ddclick\?")), callback='parse_item'),
    ]

    def parse_item(self, response):
        item = DangdangspiderItem()
        sel = Selector(response)
        e = sel.xpath("//div[@class='show_info']")

        item['title'] = e.xpath("./descendant::h1/@title").extract()
        item['author'] = e.xpath("./descendant::span[@id='author']/a[1]/text()").extract()
        item['publisher'] = e.xpath("./descendant::div[@class='messbox_info']/descendant::span[@class='t1'][2]/a/text()").extract()
        item['ptime'] = e.xpath("./descendant::div[@class='messbox_info']/descendant::span[@class='t1'][3]/text()").extract()
        item['commentnum'] =e.xpath("./descendant::div[@class='messbox_info']/descendant::div[@class='pinglun']/a[@id='comm_num_down']/text()").extract()
        item['pricename'] = e.xpath("./descendant::div[@class='price_info']/descendant::div[@class='left letter04']/text()").extract()
        item['price'] = e.xpath("./descendant::div[@class='price_info']/descendant::span[@class='price_d']/text()").extract()
        item['url'] = response.url

        return item

