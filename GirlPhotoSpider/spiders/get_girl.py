# -*- coding: utf-8 -*-
import scrapy


class GetGirlSpider(scrapy.Spider):
    name = 'get_girl'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
