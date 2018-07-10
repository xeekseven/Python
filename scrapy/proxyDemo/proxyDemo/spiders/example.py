# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['http://www.kuaidaili.com/free/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,self.parse,dont_filter=False)

    def parse(self, response):
        print("usrgo"+response.url)
        pass
