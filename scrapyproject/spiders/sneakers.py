# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
import urllib.request
import sqlite3
import csv
import os

conn = sqlite3.connect('dataX.db')
c = conn.cursor()


eleman = 0
x = 0


dosya = open("sonkullanici.txt", "r")

kullaniciadi=dosya.read()
kullaniciadi=kullaniciadi.replace(" ","")

class ToScrapeCSSSpider(scrapy.Spider):
    c.execute("CREATE TABLE IF NOT EXISTS "+str(kullaniciadi)+"(id TEXT, instalinki TEXT, postlink TEXT, takipci TEXT, takip TEXT, post TEXT, explanation NVARCHAR, like TEXT, comment TEXT, tag TEXT, date TEXT, data TEXT, location TEXT)")
    c.execute('SELECT postlink FROM '+str(kullaniciadi)+'')
    data = c.fetchall()



    name = "post"

    for row in data:
        eleman = len(data)

    dizi = [1]
    seri = dizi * (eleman)

    for row in data:
        seri[x] = row[0]
        x = x + 1

    seri = [w.replace('%20', '') for w in seri]

    try:
        for i in range (0,len(seri)+1):
            if str(seri[i]).startswith("https://pikdo.net/location")==True:
               del seri[i]
            print(str(i)+" "+seri[i])

    except:
        print("İlk çalıştırılma tamamlandı")

    start_urls = seri


    print(start_urls)



    linksirasi = 1

    def parse(self, response):
        with open("yazyazyaz.txt", "a", encoding="utf-8") as file:



            file.write("*************************************************************************(" + str(self.linksirasi) + ")*************************************************************************")

            aciklama = response.xpath('//html/body/div[3]/div[2]/div/div[1]/div/div[1]/ul/p[1]/text()').extract_first()
            if aciklama is not None:
                file.write("\nAçıklama:" + str(aciklama) + "\n")
                try:
                    c.execute("UPDATE " + str(kullaniciadi) + " SET explanation = '" + str(aciklama) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
                    conn.commit()
                except:
                    c.execute("UPDATE " + str(kullaniciadi) + " SET explanation = 'Açıklama hatalı karakter içeriyor' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
                    conn.commit()
            else:
                file.write("\nAçıklama:\n")
                try:
                    c.execute("UPDATE " + str(kullaniciadi) + " SET explanation = '" + str(aciklama) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
                    conn.commit()
                except:
                    c.execute("UPDATE " + str(kullaniciadi) + " SET explanation = 'Açıklama hatalı karakter içeriyor' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
                    conn.commit()

            like = response.xpath('//ul/li/span/text()').extract()[1]
            file.write("\nBeğeni Sayısı:" + str(like) + "\n")
            c.execute("UPDATE " + str(kullaniciadi) + " SET like = '" + str(like) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
            conn.commit()

            comment = response.xpath('//ul/li/span/text()').extract()[3]
            file.write("\nYorum Sayısı:" + str(comment) + "\n")
            c.execute("UPDATE " + str(kullaniciadi) + " SET comment = '" + str(comment) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
            conn.commit()


            hashtag = response.xpath('/html/body/div/div[2]/div/div[1]/div/div[1]/ul/p[1]/a/text()').extract()
            file.write("\nKullanılan Tagler:" + str(hashtag) + "\n")



            with open("gecici.txt", "w", encoding="utf-8") as dos:
                for row in hashtag:
                    dos.write(str(row) + " ")
                dos.close()
            oku = open("gecici.txt", "r", encoding="utf-8")
            okundu = oku.read()

            try:
                c.execute("UPDATE " + str(kullaniciadi) + " SET tag = '" + okundu + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
            except:
                c.execute("UPDATE " + str(kullaniciadi) + " SET tag = 'Hashtag hatalı karakter içeriyor' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
            conn.commit()

            tarih = response.xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[1]/ul//li[1]/span/text()').extract_first()
            file.write("\nTarih:" + str(tarih) + "\n")
            c.execute("UPDATE " + str(kullaniciadi) + " SET date = '" + str(tarih) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
            conn.commit()

            link = response.xpath('/html/head/meta[19]/@content').extract_first()
            file.write("\nPostun Linki:" + str(link) + "\n")
            c.execute("UPDATE " + str(kullaniciadi) + " SET postlink = '" + str(link) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")

            data = response.xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[1]/ul//div/img/@src').extract_first()
            try:
                os.mkdir("posts/"+kullaniciadi+"")
            except:
                print("oluştu")
            if data is None:
                data = response.xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[1]/ul/div/video/@src').extract_first()
                f = open("posts/"+kullaniciadi+"/"+str(self.linksirasi) + "_" + kullaniciadi + '.mp4', 'wb')
                f.write(urllib.request.urlopen(str(data)).read())
            else:
                f = open("posts/" + kullaniciadi + "/" + str(self.linksirasi) + "_" + kullaniciadi + '.jpg', 'wb')
                f.write(urllib.request.urlopen(str(data)).read())
            file.write("\nData Linki:" + str(data) + "\n")
            c.execute("UPDATE " + str(kullaniciadi) + " SET data = '" + str(data) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")


            lokasyon = response.xpath('/html/body/div[3]/div[2]/div/div[1]/div/div[1]/ul/figure/li[2]/a/text()').extract_first()
            if lokasyon is not None:
                file.write("\nKonum:" + str(lokasyon) + "\n")
                c.execute("UPDATE " + str(kullaniciadi) + " SET location = '" + str(lokasyon) + "' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
                conn.commit()
            else:
                file.write("\nKonum belirtilmemiştir\n")
                c.execute("UPDATE " + str(kullaniciadi) + " SET location = 'Konum belirtilmemiştir' WHERE id = '"+str(self.linksirasi)+"_"+kullaniciadi+"'")
                conn.commit()
        with open("araba.txt", "w", encoding="utf-8") as yazdir:
            yazdir.write(str(self.linksirasi) + " ")
        with open("motor.txt", "w", encoding="utf-8") as yazdirt:
            yazdirt.write(str(len(self.seri)) + " ")

        for i in range (len(self.seri)+1,len(self.seri)+200):
            c.execute("DELETE FROM " + kullaniciadi + " WHERE id = '"+str(i)+"_"+kullaniciadi+"'")
            conn.commit()

        self.linksirasi += 1

#        for i in range (self.linksirasi+1,len(self.seri)+1):
#            c.execute("DELETE FROM " + kullaniciadi + " WHERE id = '"+str(i)+"_"+kullaniciadi+"'")
#        conn.commit()

