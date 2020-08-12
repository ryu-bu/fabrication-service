import smtplib, ssl
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

class EMAIL:
    port = ""
    sender = ""
    password = ""
    def __init__(self):
        self.sender = os.getenv('SENDER')
        self.password = os.getenv('PASSWORD')
        self.port = 465

    def send_email(self, receive, type, id):
        # message = ("From: %s\r\nTo: %s\r\n\r\n" % ("Fab Services", receive))
        msg = MIMEMultipart()
        
        if type == 'sub':
            subject = "Submission Confirmation ID: " + str(id)
            content = "Your record has been submitted successfully and will be reviewed shortly."
        elif type == 'man':
            subject = "New Submission ID: " + str(id)
            content = "New record has been submitted."
        elif type == 'fabAcc':
            subject = "ID: " + str(id) + " Accepted"
            content = "Your submission has been accepted."
        elif type == 'fabRej':
            subject = "ID: " + str(id) + " Rejected"
            content = "Your submission has been rejected."
        elif type == 'mac':
            subject = "New Request ID: " + str(id)
            content = "New job has been requested."
        else:
            subject = "Order ID: " + str(id) + " Completed"
            content = "Your order has been completed."

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