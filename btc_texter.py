import smtplib
import json
import urllib2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# opens up the API and extracts information from the JSON
url = "https://api.gemini.com/v1/pubticker/btcusd"
data = json.load(urllib2.urlopen(url))
message = data["last"]
print (message)
info = open("userinfo","r")

# create message object instance
msg = MIMEMultipart()


# setup the parameters of the message
password = info.readline()
msg['From'] = info.readline()
msg['To'] = info.readline()

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print ("Successfully sent email to %s:" % (msg['To']))