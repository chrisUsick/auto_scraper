# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re

def serialize_number(value):
    regex = re.compile('[\d,.]+')
    commas = re.compile(',')
    return float(commas.sub('', regex.search(value).group()))

def serialize_kilometers(value):
    kms = re.compile('(km|kms)')
    match = kms.search(value)
    if match:
        return serialize_number(value)
    else:
        return serialize_number(value)/1.6


class Vehicle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    kilometers = scrapy.Field(serializer=serialize_kilometers)
    price = scrapy.Field(serializer=serialize_number)
    url = scrapy.Field()
    transmission = scrapy.Field()
    drive = scrapy.Field()
    body_style = scrapy.Field()
    img_url = scrapy.Field()
    site = scrapy.Field()
