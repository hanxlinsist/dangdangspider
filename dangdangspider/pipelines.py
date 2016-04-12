# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class DangdangspiderPipeline(object):

    threshold = 70

    def __init__(self):
        print 'this is init method'

    def process_item(self, item, spider):

        # 评论数
        conum = int(item['commentnum'][0])
        
        if  item['title'] and item['commentnum']:
            if self.threshold < conum:
                return item
            else:
                raise DropItem('commentnum less than 70, so drop it')
        else:
            raise DropItem('some items is null,so drop it')

        

