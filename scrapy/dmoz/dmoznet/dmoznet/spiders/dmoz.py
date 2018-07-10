# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dmoznet.items import DmoznetItem 


class DmozSpider(CrawlSpider):
    name = 'dmoz'
    redis_key = 'DmozSpider:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'http://dmoztools.net/.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DmoznetItem()
        item['url'] = response.url
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
