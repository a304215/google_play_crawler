# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GooglePlayCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    name = scrapy.Field()
    last_updated = scrapy.Field()
    author = scrapy.Field()
    filesize = scrapy.Field()
    downloads = scrapy.Field()
    version = scrapy.Field()
    requires_android = scrapy.Field()
    content_rating = scrapy.Field()
    genre = scrapy.Field()
    price = scrapy.Field()
    rating_value = scrapy.Field()
    review_number = scrapy.Field()
    pass
