# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis

class DmoznetPipeline(object):

    '''
    def open_spider(self, spider):
        self.conn = redis.Redis(host='127.0.0.1', port=6379,db=0)
    
    def close_spider(self, spider):
        pass
    '''
    def process_item(self, item, spider):
        #self.conn.lpush("dz:urls",item)
        print(item['url'])
        return item
