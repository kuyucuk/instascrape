# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(link TEXT)")

url="https://pikdo.net/u/acunilicali/270350200"
say=0

class MySpider(scrapy.Spider):
    name = "insta2"


    start_urls = [
        url
    ]
    c.execute('SELECT * FROM stuffToPlot')
    def parse(self, response):

        global say
        with open("yazyazyaz.txt", "a", encoding="utf-8") as file:

            for link in response.xpath("//html/body"):
                link = link.xpath('//*[@id="ShowPhotos"]/div/div[1]/div/div/ul/li/a/@href').extract()
            file.write(str(link))
            print("\nLink:" + str(link) + "\n")

            b=str([' Neueste'])

            linko = response.xpath('//*[@id="ShowPhotos"]/div/div[2]/a/text()').extract()

            if say==0:
                next_url = response.css('div.showMore a::attr(href)').extract()[0]
                say = say + 1
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
            else:
                if str(linko) != b:
                    next_url= response.css('div.showMore a::attr(href)').extract()[1]
                    yield  scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

            dosya = open("yazyazyaz.txt", "r")
            print(dosya.read())