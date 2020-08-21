import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:

    def __init__(self):
        self.sender = os.getenv('SENDER')
        self.password = os.getenv('PASSWORD')
        self.port = 465

    def send_email(self, receive, subject, content):
        # message = ("From: %s\r\nTo: %s\r\n\r\n" % ("Fab Services", receive))
        msg = MIMEMultipart()

        content += "\r\n\nFab Services"

        msg['From'] = "Fab Services"
        msg['To'] = receive
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))
        message = msg.as_string()
        context = ssl.create_default_context()


        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, receive, message)