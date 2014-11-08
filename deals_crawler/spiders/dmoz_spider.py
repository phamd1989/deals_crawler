__author__ = 'dung'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from deals_crawler.items import DealsCrawlerItem

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.urbanspoon.com/n/21/2045/Philadelphia/University-City-restaurants",
    ]
    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       titles = hxs.select('//a[contains(@href, "/r")]')
       addresses = hxs.select('//span[contains(@class,"address")]')
       items = []
       print 'SSDSDDS'
       i = 0
       while i<=14:
          print i
          item = DealsCrawlerItem()
          item['name'] = titles[i].select('@title').extract()
          item['address'] = addresses[i].select('text()').extract()
          i = i + 1
          items.append(item)
       return items