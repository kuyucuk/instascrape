"""
# -*- coding: utf-8 -*-
import sqlite3
import csv
import os

def convert ():
    bagla = sqlite3.connect('data.db')

    sec = bagla.cursor()
    sec.execute('SELECT * FROM stuffToPlot')

    with open("out.csv", "w", newline='') as csv_file:  # Python 3 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in sec.description])  # write headers
        csv_writer.writerows(sec)

    f = open('out.csv')
    csv_f = csv.reader(f)
    data = []

    for row in csv_f:
        data.append(row)
    f.close()

    def convert_row(row):
        return """  """<row>
        <marka>%s</marka>
        <model>%s</model>
        <cins>%s</cins>
        <renk>%s</renk>
        <numaralar>%s</numaralar>
        <IMG_url>%s</IMG_url>
        <stok>%s</stok>
        <url>%s</url>
        <ozelliker>%s</ozelliker>
        <aciklama>%s</aciklama>
        <eski_fiyat>%s</eski_fiyat>
        <yeni_fiyat>%s</yeni_fiyat>
 #     </row> % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

   data = ""<?xml version="1.0" encoding="UTF-8"?>
#    <root>
#    "" + '\n'.join([convert_row(row) for row in data[1:]]) + """
#    </root>"""
"""
    file = open("output.xml", "w", encoding="utf-8")

    veri = str(data).replace("&h=", "&amp;h=")
    file.write(veri)
    file.close()

    file = open("output.xml", "w", encoding="utf-8")
    veri = veri.replace("&qlt=", "&amp;qlt=")
    file.write(veri)
    file.close()


    # print (veri)

    file = open("output.xml", "r", encoding="utf-8")

    dosya = file.read()
    print(dosya)

    file = open("dataX.xml", "w", encoding="utf-8")
    degisim = str(dosya).replace("FIELD1>", "ProductName>")
    file.write(degisim)
    file.close()


    print(degisim)

convert()
"""