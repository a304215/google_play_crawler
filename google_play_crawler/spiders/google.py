import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import GooglePlayCrawlerItem
from urllib.parse import urlparse

class GoogleSpider(CrawlSpider):
    name = 'google'
    allowed_domains = ['play.google.com']
    start_urls = ["https://play.google.com/store/apps/"]

    rules = (
        Rule(LinkExtractor(allow=('/store/apps',), deny=('/store/apps/details', )), follow=True),
        Rule(LinkExtractor(allow=("/store/apps/details", )), follow=True, callback='parse_detail'),
    )

    def parse_detail(self,response):
        items = []
        for title in response.xpath('/html'):
            item = GooglePlayCrawlerItem()
            item["link"] = title.xpath('head/link[5]/@href').extract_first()
            item["name"] = title.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span/text()').extract_first()
            item["last_updated"] = title.xpath('//div[contains(text(), "Updated")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["author"] = title.xpath('//div[contains(text(), "Offered By")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["filesize"] = title.xpath('//div[contains(text(), "Size")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["downloads"] = title.xpath('//div[contains(text(), "Installs")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["version"] = title.xpath('//div[contains(text(), "Current Version")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["requires_android"] = title.xpath('//div[contains(text(), "Requires Android")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["content_rating"] = title.xpath('//div[contains(text(), "Content Rating")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["genre"] = title.xpath('//a[@itemprop="genre"]/text()').extract_first()
            item["price"] = title.xpath('//meta[@itemprop="price"]/@content').extract_first()
            item["rating_value"] = title.xpath('//div[@class="K9wGie"]/div/text()').extract_first()
            item["review_number"] = title.xpath('//span[@class="EymY4b"]/span[2]/text()').extract_first()
            yield item
