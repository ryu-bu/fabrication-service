from emailapi import Email
from models.fabricationitem import FabricationItem

class FabricationControl:
    def __init__(self, json_data=[]):
        self.json_data = json_data
        self.id = json_data['order_id']
        self.email_addr = json_data['email']
        self.email = Email()

    def process_fabrication(self, command):
        if command == 'fabAcc':
            # update sub db command
            subject = "ID: " + str(self.id) + " Accepted"
            content = "Your submission has been accepted."
            fabrication = FabricationItem(**self.json_data)
            fabrication.save()
        elif command == 'mac':
            # send to fab db command
            subject = "New Request ID: " + str(self.id)
            content = "New job has been requested."
            self.email_addr = 'ryuichi1174@gmail.com'
        else:
            # update dab db
            subject = "Order ID: " + str(self.id) + " Completed"
            content = "Your order has been completed."
            fabrication = FabricationItem.objects(order_id=self.id)
            fabrication.update(**self.json_data)
        
        self.email.send_email(self.email_addr, subject, content)