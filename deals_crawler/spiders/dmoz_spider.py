__author__ = 'dung'

from scrapy.spider import BaseSpider
from deals_crawler.items import DealsCrawlerItem

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.offers.com/offers/in-store/"]

    def parse(self, response):
        types =  response.xpath("//div[@class='top-message']/text()")
        images = response.xpath("//div[@class='offer-image']")
        info = response.xpath("//div[@class='offer-info']")
        prepend_url = "http://www.offers.com"

        # remember to add defensive code here
        # by checking the minimum length among those 3

        items = []
        i = 0
        while i<=29:
            print i
            item = DealsCrawlerItem()
            item['type']          = types[i].extract()
            item['image_url']     = images[i].xpath('a/img/@src').extract()
            item['title']         = info[i].xpath('p/a/@title').extract()
            item['company_name']  = info[i].xpath("div[@class='clearfix']/span/a/@title").extract()
            deal                  = info[i].xpath("div[@class='clearfix']/span/a/@href").extract()
            item['company_deals'] = prepend_url + ''.join(deal)
            url                   = info[i].xpath("div[@class='buy']/div[@class='buy-button button-outer  noncom']/@data-href")\
                                           .extract()
            print url
            item['deal_url']      = prepend_url + ''.join(url)
            i = i + 1
            items.append(item)
        return items