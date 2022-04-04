import smtplib, ssl
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from bs4 import BeautifulSoup as bs
import os

port = 587
allGraphs_path = os.path.abspath(os.curdir) + "\\TechnicalSide\\Temp\\"
Sender = "smarket_alert@outlook.com"
Reciever = ""
Subject = "The price of ... got up, hurry up!"
password = "12Op6gS_yhUPq1_"
context = ssl.create_default_context()  

def SendMail(message):
	global Sender

	with smtplib.SMTP("smtp-mail.outlook.com", port) as server:
		server.starttls(context = context)
		server.login(Sender, password)
		server.sendmail(Sender, "slowtv583@gmail.com", message)
		server.quit()

def Make_letter():
	global Sender

	html = "Here's the price of 3M came to <b>145!</b> <br> <img src = "+ allGraphs_path +"3M.png>"
	text = bs(html, "html.parser").get_text()

	message = MIMEMultipart("alternative")
	message["To"] = "slowtv583@gmail.com"
	message["From"] = Sender
	message["Subject"] = Subject

	text_part = MIMEText(text, "plain")
	html_part = MIMEText(html, "html")
	Image_Part = MIMEApplication(open(allGraphs_path + "3M.png", 'rb').read())
	Image_Part.add_header('Your Candle-Graph', 'attachment', filename='3M.png')

	message.attach(text_part)
	message.attach(html_part)
	message.attach(Image_Part)

	SendMail(message.as_string())

Make_letter()