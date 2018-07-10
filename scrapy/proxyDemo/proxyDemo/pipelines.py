# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import os

class ProxydemoPipeline(object):
    
    def __init__(self):
        if not os.path.exists('proxy_ip.db'):
            sqlconn = sqlite3.connect('proxy_ip.db')
            sqlconn.cursor().execute('create table ip( ip_addr Text,port int )')
            sqlconn.commit()
            sqlconn.close()
    def open_spider(self,spider):
        self.conn = sqlite3.connect('proxy_ip.db')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sqlText = 'insert into ip(ip_addr,port) values("{0}",{1})'.format(item['ip'],int(item['port']))
        print(sqlText)
        self.cur.execute(sqlText)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
