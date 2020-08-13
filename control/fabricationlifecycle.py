from emailapi import EMAIL

class FabricationControl:
    def __init__(self, json_data=[]):
        self.json_data = json_data
        self.id = json_data['id']
        self.emailAddr = json_data['email']
        self.email = EMAIL()

    def ProcessFabrication(self, command):
        if command == 'fabAcc':
            # update sub db command
            subject = "ID: " + str(self.id) + " Accepted"
            content = "Your submission has been accepted."
        elif command == 'mac':
            # send to fab db command
            subject = "New Request ID: " + str(self.id)
            content = "New job has been requested."
            self.emailAddr = 'ryuichi1174@gmail.com'
        else:
            # update dab db
            subject = "Order ID: " + str(self.id) + " Completed"
            content = "Your order has been completed."
        
        self.email.send_email(self.emailAddr, subject, content)