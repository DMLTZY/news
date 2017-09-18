# -*- coding: utf-8 -*-
import scrapy
from news.items import BaiduItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/']
    custom_settings = {
        'FEED_URI': 'baidu-feed.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'FEED_EXPORT_FIELDS': ['title', 'href'],
    }

    def parse(self, response):
        # news_block = response.xpath(
        #     "//div[@id='pane-news']/ul[@class='ulist focuslistnews']/"
        #     "li[@class='bold-item']"
        # )
        news = response.xpath(
            "//div[@id='pane-news']/div[@class='hotnews']/"
            "ul/li/strong"
        )
        for n in news:
            item = BaiduItem()
            item['title'] = n.xpath(
                "a/text()"
            ).extract()[0]
            item['href'] = n.xpath(
                "a/@href"
            ).extract()[0]
            yield item
        pass
