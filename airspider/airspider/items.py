# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    quality = scrapy.Field()
    city = scrapy.Field()
    province = scrapy.Field()
    aqi = scrapy.Field()
    pm25 = scrapy.Field()
