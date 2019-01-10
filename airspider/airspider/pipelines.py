# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AirspiderPipeline(object):
	def __init__(self):
		self.file = open('air-level.txt', 'w')	#保存成格式化的数据列表
		self.jsonfile = open('air-level.json', 'w')
	def close_spider(self, spider):
		self.file.close()
		self.jsonfile.close()

	def process_item(self, item, spider):
		self.file.write(item['rank'] + "\t\t" + item['quality'] + "\t\t" + item['city'] + "\t\t" + item['province']
						+ "\t\t" + item['aqi'] + "\t\t" + item['pm25'] + "\n")
		self.jsonfile.write(json.dumps(dict(item)) + "\n")
		return item
