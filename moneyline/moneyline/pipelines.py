# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from moneyline.items import GameItem
import datetime

class MoneylinePipeline(object):
	def process_item(self, item, spider):
		item.save()
		print('||||||||||')
		print(type(item))
		print('||||||||||')
		return item
#		print(item.keys())
