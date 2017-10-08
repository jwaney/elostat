# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field
from scrapy_djangoitem import DjangoItem
from scrapeSBRodds.models import Game

#class MoneylineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass

class GameItem(DjangoItem):
	print('|||||||||||||||||||||||FUCK THIS|||||||||||||||||||||||||||')
	django_model = Game
