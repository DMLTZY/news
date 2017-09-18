# coding:utf-8
import scrapy
from news.items import QQItem


class QQSpider(scrapy.Spider):
    name = 'qq'
    allowed_domains = ['news.qq.com']
    start_urls = ['http://news.qq.com/']

    def parse(self, response):
        item = QQItem()
        head = response.xpath(
            "//div[@class='head']/div[@id='subHot']/h2"
        )
        item['title'] = head.xpath(
            "a/text()"
        ).extract()[0]
        item['href'] = head.xpath(
            "a/@href"
        ).extract()[0]
        yield item

        # item = QQItem()
        slist = response.xpath(
            "//div[@class='head']/div[@id='subHot']/"
            "div[@class='slist']/ul/li"
        )
        for a in slist:
            item['title'] = a.xpath(
                "a/text()"
            ).extract()[0]
            item['href'] = a.xpath(
                "a/@href"
            ).extract()[0]
            yield item
