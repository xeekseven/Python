# -*- coding: utf-8 -*-
import scrapy


class QiyuanspiderSpider(scrapy.Spider):
    name = 'qiyuanSpider'
    allowed_domains = ['https://detail.1688.com/offer/520275058038.html?spm=a2615.7691456.0.0.d3059e2XM18SA']
    start_urls = ['http://https://detail.1688.com/offer/520275058038.html?spm=a2615.7691456.0.0.d3059e2XM18SA/']

    def start_requests()

    def parse(self, response):
        pass
