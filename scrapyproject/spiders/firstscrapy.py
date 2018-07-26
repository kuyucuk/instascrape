# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

kullanici="gezmekteyim"


url="https://pikdo.net/search/"+kullanici+""


class MySpider(scrapy.Spider):
    name = "firstscrapy"

    start_urls = [
        url
    ]

    def parse(self, response):
        sitelinki=response.xpath('/html/body/div[4]/div[1]/ul[1]/li[1]/div/a/@href').extract_first()
        with open("link.txt", "w", encoding="utf-8") as dosya:
            dosya.write(sitelinki)

