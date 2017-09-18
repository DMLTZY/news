# coding:utf-8
import scrapy
from news.items import WangYiItem


class QQSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    def parse(self, response):
        item = WangYiItem()
        heads = response.xpath(
            "//div[@class='mod_top_news2']/h2"
        )
        for h in heads:
            item['title'] = h.xpath(
                "a/text()"
            ).extract()[0]
            item['href'] = h.xpath(
                "a/@href"
            ).extract()[0]
            yield item

        top_news_ul = response.xpath(
            "//div[@class='mod_top_news2']/ul[@class='top_news_ul']/li/a"
        )
        for a in top_news_ul:
            item['title'] = a.xpath(
                "text()"
            ).extract()[0]
            item['href'] = a.xpath(
                "@href"
            ).extract()[0]
            yield item
