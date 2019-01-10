# -*- coding: utf-8 -*-
import scrapy
from airspider.items import AirspiderItem

class GetairSpider(scrapy.Spider):
    name = 'getair'
    allowed_domains = ['pm25.com']
    start_urls = ['http://www.pm25.com/rank.html']

    def parse(self, response):
        for i in range(1,300):
            item = AirspiderItem()
            i = str(i)
            item['rank'] = response.xpath("/html/body/div[5]/div/div[3]/ul[2]/li["+i+"]/span[1]/text()").extract()[0]
            item['quality'] = response.xpath("/html/body/div[5]/div/div[3]/ul[2]/li["+i+"]/span[2]/em/text()").extract()[0]
            item['city'] = response.xpath("/html/body/div[5]/div/div[3]/ul[2]/li["+i+"]/a/text()").extract()[0]
            item['province'] = response.xpath("/html/body/div[5]/div/div[3]/ul[2]/li["+i+"]/span[3]/text()").extract()[0]
            item['aqi'] = response.xpath("/html/body/div[5]/div/div[3]/ul[2]/li["+i+"]/span[4]/text()").extract()[0]
            item['pm25'] = response.xpath("/html/body/div[5]/div/div[3]/ul[2]/li["+i+"]/span[5]/text()").extract()[0]
            yield item
