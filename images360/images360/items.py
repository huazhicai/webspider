# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class ImageItem(Item):
    # mongodb 和 mysql 表名
    collection = table = 'images'
    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
    pass
