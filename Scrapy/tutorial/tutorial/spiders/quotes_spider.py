#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Project: PythonSpider
# @Date: 2019/1/19
# @Author: MatthewP

import scrapy


class QuotesSpider(scrapy.Spider):
    # Spider id. 同一个爬虫项目必须使用同一个id。同时不能与其他项目重名。
    name = 'quotes'

    # start_requests方法必须返回可迭代的Requests对象。
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.xpath('//div/quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
            }
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)