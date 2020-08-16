from emailapi import Email
from models.fabricationitem import FabricationItem

class FabricationControl:
    def __init__(self, json_data=[]):
        self.json_data = json_data
        self.id = json_data['order_id']
        self.email = Email()

    def process_fabrication(self, command):
        # send acceptance email to the user
        if command == 'fabAcc':
            subject = "ID: " + str(self.id) + " Accepted"
            content = "Your submission has been accepted."

            # create new record on db
            fabrication = FabricationItem(**self.json_data)
            fabrication.save()
            email_addr = self.json_data['email']

        # send job notication to machinist
        elif command == 'mac':
            subject = "New Request ID: " + str(self.id)
            content = "New job has been requested."
            email_addr = 'ryuichi1174@gmail.com'

        # when a record is updated
        else:
            subject = "Order ID: " + str(self.id) + " Completed"
            content = "Your order has been completed."

            # update db + email logic
            fabrication = FabricationItem.objects.get(order_id=self.id) # get one record
            prev_status = fabrication['stage']
            fabrication.update(**self.json_data)
            cur_item = FabricationItem.objects.get(order_id=self.id)

            if prev_status == cur_item['stage'] or cur_item['stage'] != 'completed': # send completion email only for the first time
                return
            email_addr = cur_item['email']
        
        self.email.send_email(email_addr, subject, content)