# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re

def serialize_price(value):
    regex = re.compile('[\d,.]+')
    commas = re.compile(',')
    return float(commas.sub('', regex.search(value).group()))

class Vehicle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    kilometers = scrapy.Field()
    price = scrapy.Field(serializer=serialize_price)
