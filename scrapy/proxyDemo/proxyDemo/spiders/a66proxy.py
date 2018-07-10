# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from proxyDemo.items import ProxydemoItem


class A66proxySpider(CrawlSpider):
    name = '66proxy'
    allowed_domains = ['www.66ip.cn']
    start_urls = ['http://www.66ip.cn/areaindex_1/1.html']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.66ip.cn/areaindex_\d{1,2}/\d{1,2}.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ProxydemoItem()
        #response.xpath('//div[@id="footer"]/div/table/tbody/tr')[0].xpath('./td/text()').extract()
        ipTrList = response.xpath('//div[@id="footer"]//table/tr')
        for ipItem in ipTrList:
            #print(ipItem.xpath('./td[@data-title="IP"]/text()').extract()[0])
            ip = ipItem.xpath('./td/text()').extract()[0]  if ipItem.xpath('./td/text()').extract()[0] != None else '0.0.0.0'
            port = ipItem.xpath('./td/text()').extract()[1]  if ipItem.xpath('./td/text()').extract()[1] != None  else '0'
            server = 'http://'+ ip + ':'+ port
            print("开始检测:"+server)
            try:
                requests.get('http://www.baidu.com', proxies={"http":server},timeout=3)
            except:
                print('connect failed')
                pass
            else:
                print("success ip:"+server)
                item['ip'] = ip
                item['port'] = port
                return item
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        pass
