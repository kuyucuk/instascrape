# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3
import os

conn = sqlite3.connect('dataX.db')
c = conn.cursor()

sitelinki = open("link.txt", "r")
url=sitelinki.read()

try:
    os.mkdir("posts")
except:
    print("posts zaten oluşturulmuş")
artan=0
say=0

class MySpider(scrapy.Spider):
    name = "profil"


    start_urls = [
        url
    ]

    def parse(self, response):
        global say, artan
        with open("yazyazyaz.txt", "a", encoding="utf-8") as file:



            file.write("\n\n\n********************************************************************************\n")
            kullaniciadi = response.xpath('/html/body/div[4]/div[1]/div[2]/h1/text()').extract_first()
            kullaniciadi = kullaniciadi.replace(" ", "")
            instalinki= "https://www.instagram.com/" + str(kullaniciadi) +""
            print("\nLink: "+instalinki+"\n")
            file.write("\nLink: "+instalinki+"\n")

            with open("sonkullanici.txt", "w", encoding="utf-8") as dosya:
                dosya.write(kullaniciadi)
            if say == 0:
                try:
                    c.execute("DELETE FROM " + kullaniciadi + "")    #önceki dataları silmek için
                    conn.commit()
                except:
                    print("Daha böyle bir tablo oluşturulmamış")
            c.execute("CREATE TABLE IF NOT EXISTS " + str(kullaniciadi) + "(id TEXT, instalinki TEXT, postlink TEXT, takipci TEXT, takip TEXT, post TEXT, explanation TEXT, like TEXT, comment TEXT, tag TEXT, date TEXT, data TEXT, location TEXT)")
            c.execute('SELECT * FROM ' + str(kullaniciadi) + '')

            for takipci in response.xpath("//html/body"):
                takipci = takipci.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[2]//strong/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nTakipçi:" + str(takipci) + "\n")
            print("\nTakipçi:" + str(takipci) + "\n")

            for takip in response.xpath("//html/body"):
                takip = takip.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[3]//strong/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nTakip:" + str(takip) + "\n")
            print("\nTakip:" + str(takip) + "\n")

            for post in response.xpath("//html/body"):
                post = post.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[1]//strong/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nPost:" + str(post) + "\n")
            print("\nPost:" + str(post) + "\n")
            """
            for marka in response.css("a.media-detail"):
                yazar = marka.xpath('//a/@href').extract()
            file.write("\nMarka:" + str(yazar) + "\n")
            """
            for link in response.xpath("//html/body"):
                link = link.xpath('//*[@id="ShowPhotos"]/div/div[1]/div/div/ul/li/a/@href').extract()
            file.write("________________________________________________________________________________")
            file.write("\nLink:" + str(link) + "\n")
            print("\nLink:" + str(link) + "\n")


            file.write("\n********************************************************************************\n")

            """
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
            """
            for i in range (0,60):

#               if len(response.xpath('//*[@id="ShowPhotos"]/div/div[1]/div/div/ul/li/a/@href').extract()[i])>60:
                    c.execute("INSERT INTO " + str(kullaniciadi) + " VALUES('"+str(artan+1)+"_" + str(kullaniciadi)+"','"+str(instalinki)+"', '"+ link[i]+"?hl=tr"+"','"+str(takipci)+"','"+str(takip)+"','"+str(post)+"','-','-','-','-','-','-','-')")
                    conn.commit()
                    artan=artan+1
            c.close()
            conn.close()




























#ikinci kod


"""

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
    name = "insta"


    start_urls = [
        url
    ]
    c.execute('SELECT * FROM stuffToPlot')
    def parse(self, response):

        global say
        with open("yazyazyaz.txt", "a", encoding="utf-8") as file:

            file.write("\n\n\n********************************************************************************\n" + url + "\n")
            kullaniciadi = response.xpath('/html/body/div[4]/div[1]/div[2]/h1/text()').extract_first()
            print("\nLink: https://www.instagram.com/" + str(kullaniciadi) + "\n")

            for takipci in response.xpath("//html/body"):
                takipci = takipci.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[2]/strong/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nTakipçi:" + str(takipci) + "\n")
            print("\nTakipçi:" + str(takipci) + "\n")

            for takip in response.xpath("//html/body"):
                takip = takip.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[3]/strong/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nTakip:" + str(takip) + "\n")
            print("\nTakip:" + str(takip) + "\n")

            for post in response.xpath("//html/body"):
                post = post.xpath('/html/body/div[4]/div[1]/div[2]/ul/li[1]//strong/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nPost:" + str(post) + "\n")
            print("\nPost:" + str(post) + "\n")

            for link in response.xpath("//html/body"):
                link = link.xpath('//*[@id="ShowPhotos"]/div/div[1]/div/div/ul/li/a/@href').extract()
            file.write("________________________________________________________________________________")
            file.write("\nLink:" + str(link) + "\n")
            print("\nLink:" + str(link) + "\n")

            b=str([' Neueste'])

            file.write("\n********************************************************************************\n")


            linko = response.xpath('//*[@id="ShowPhotos"]/div/div[2]/a/text()').extract()

            if say==0:
                next_url = response.css('div.showMore a::attr(href)').extract()[0]
                say = say + 1
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
            else:
                if str(linko) != b:
                    next_url= response.css('div.showMore a::attr(href)').extract()[1]
                    yield  scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

"""






#ilk kod




"""


# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(link TEXT)")



class MySpider(scrapy.Spider):
    name = "insta"

    kullaniciadi=input("\nKullanıcı Adı Giriniz: ")
    start_urls = [
        'http://picbear.online/'+kullaniciadi+''
    ]
    c.execute('SELECT * FROM stuffToPlot')
    def parse(self, response):

        with open("yazyazyaz.txt", "a", encoding="utf-8") as file:

            file.write("\n\n\n********************************************************************************\n"+self.kullaniciadi+"\n")
            print("\nKullanıcı Adı:" + str(self.kullaniciadi) + "\n")

            for takipci in response.xpath("//html/body"):
                takipci = takipci.xpath('/html/body/div[3]/div[1]/div/div/div/div[2]/ul[1]/li[2]/span/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nTakipçi:" + str(takipci) + "\n")
            print("\nTakipçi:" + str(takipci) + "\n")

            for takip in response.xpath("//html/body"):
                takip = takip.xpath('/html/body/div[3]/div[1]/div/div/div/div[2]/ul[1]/li[3]/span/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nTakip:" + str(takip) + "\n")
            print("\nTakip:" + str(takip) + "\n")

            for post in response.xpath("//html/body"):
                post = post.xpath('/html/body/div[3]/div[1]/div/div/div/div[2]/ul[1]/li[1]/a/span/text()').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nPost:" + str(post) + "\n")
            print("\nPost:" + str(post) + "\n")

            for marka in response.css("a.media-detail"):
                yazar = marka.xpath('//a/@href').extract()
            file.write("\nMarka:" + str(yazar) + "\n")

            for link in response.xpath("//html/body"):
                link = link.xpath('/html/head/link[3]/@href').extract()[0]
            file.write("________________________________________________________________________________")
            file.write("\nLink:" + str(link) + "\n")
            print("\nLink:" + str(link) + "\n")

            file.write("\n********************************************************************************\n")

            c.execute("INSERT INTO stuffToPlot VALUES('" + str(link) + "')")
            conn.commit()





"""
