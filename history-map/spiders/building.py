# -*- coding: utf-8 -*-

from datetime import datetime

from scrapy.spider import Spider

from history-map.items import TV


class BuildingSpider(Spider):
    name = 'building'
    allowed_domains = ['www.hzfc.gov.cn']
    start_urls = (
        'http://www.hzfc.gov.cn/lb/lsjz.php?getgroupname=%B5%DA%D2%BB%C5%FA',
    )

    def parse(self, response):
        # pass
