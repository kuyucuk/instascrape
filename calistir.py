import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#subprocess.check_output(['ls','-l']) #all that is technically needed...
#Totokuyu

def cagir():
    username=input("Kullanıcı Adını Giriniz")

os.system("scrapy crawl insta")
