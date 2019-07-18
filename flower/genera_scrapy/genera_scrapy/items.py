# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GeneraScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    #字段名称根据项目定义，相当于数据库表里面的字段,该对象相当于ORM工具生成的数据库表对象
    # name = scrapy.Field()
    # population = scrapy.Field()
    name = scrapy.Field()
    imgurl = scrapy.Field()
    imgherf = scrapy.Field()
    imgvisit = scrapy.Field()
    imglike = scrapy.Field()
    imgdiscrit = scrapy.Field()