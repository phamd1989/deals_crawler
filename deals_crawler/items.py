# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DealsCrawlerItem(scrapy.Item):
    type = scrapy.Field()
    image_url = scrapy.Field()
    title = scrapy.Field()
    deal_url = scrapy.Field()
    company_name = scrapy.Field()
    company_deals = scrapy.Field()