# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from proxyDemo.items import ProxydemoItem


class KuaidlSpider(CrawlSpider):
    name = 'KuaiDL'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/intr']

    rules = (
        #Rule(LinkExtractor(allow=r'http://www.kuaidaili.com/fr'),callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=r'http://www.kuaidaili.com/free/intr/\d+/$'), callback='parse_item', follow=True),
    )
    #allow=r'http://www.kuaidaili.com/free/inha/.+'
    def parse_item(self, response):
        item = ProxydemoItem()
        ipTrList = response.xpath('//div[@id="list"]/table/tbody/tr')
        for ipItem in ipTrList:
            #print(ipItem.xpath('./td[@data-title="IP"]/text()').extract()[0])
            ip = ipItem.xpath('./td[@data-title="IP"]/text()').extract()[0]  if ipItem.xpath('./td[@data-title="IP"]/text()').extract()[0] != None else '0.0.0.0'
            port = ipItem.xpath('./td[@data-title="PORT"]/text()').extract()[0]  if ipItem.xpath('./td[@data-title="PORT"]/text()').extract()[0] != None  else '0'
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
        #print(response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        pass