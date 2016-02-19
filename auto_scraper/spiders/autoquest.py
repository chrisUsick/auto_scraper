# -*- coding: utf-8 -*-
import scrapy
from auto_scraper.items import Vehicle


class AutoquestSpider(scrapy.Spider):
    name = "autoquest"
    allowed_domains = ["autoquestwinnipeg.com"]
    start_urls = [
        'http://www.autoquestwinnipeg.com/used-inventory/index.htm'
    ]

    def parse(self, response):
        for href in response.selector.css('li.item .hproduct h1 a::attr("href")'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_vehicle)
        next_page = response.selector.css('.ft2 .paging .mod > a::attr("href")')[0].extract()
        url = response.urljoin(next_page)
        yield scrapy.Request(url, callback=self.parse)
    def parse_vehicle(self, response):
        """
        :type response: scrapy.http.Response
        """
        item = Vehicle()
        item['name'] = response.css(".bd2 > h1::text")[0].extract()
        item['year'] = response.css('ul.details > li.year span::text')[0].extract()
        item['make'] = response.css('ul.details > li.make span::text')[0].extract()
        item['model'] = response.css('ul.details > li.model span::text')[0].extract()
        item['kilometers'] = response.css('ul.details > li.odometer span::text')[0].extract()
        item['price'] = response.css('ul.pricing > li > span strong.price::text')[0].extract()
        item['url'] = response.url
        item['transmission'] = response.css('ul.details > li.transmission span::text')[0].extract()
        item['drive'] = response.css('ul.details > li.driveLine span::text')[0].extract()
        item['body_style'] = response.css('ul.details > li.bodyStyle span::text')[0].extract()
        item['img_url'] = response.css('.imageViewer a img::attr(src)')[0].extract()
        item['site'] = response.url
        yield item
