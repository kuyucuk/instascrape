import os
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
#subprocess.check_output(['ls','-l']) #all that is technically needed...
#Totokuyu

os.system("scrapy crawl firstscrapy")
os.system("scrapy crawl profil")
os.system("scrapy crawl post")








