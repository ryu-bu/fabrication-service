from emailapi import Email
from models.submissionitem import SubmissionItem

class SubmissionControl:

    #sTEP 1 - save the data

    #step 2 - Do whaterever you need to do

    #Step 3 - send the notifications

    def __init__(self, json_data=[]):
        self.json_data = json_data
        self.id = json_data['order_id']
        self.email = Email()

    def process_submission(self, command):
        if command == 'sub':
            # send to sub db 
            subject = "Submission Confirmation ID: " + str(self.id)
            content = "Your record has been submitted successfully and will be reviewed shortly."

            # create new record on db
            submission = SubmissionItem(**self.json_data)
            submission.save()
            email_addr = self.json_data['email']

        elif command == 'man':
            subject = "New Submission ID: " + str(self.id)
            content = "New record has been submitted."
            email_addr = 'ryuichi1174@gmail.com'
            
        elif command == 'fabRej':
            # update sub db command
            subject = "ID: " + str(self.id) + " Rejected"
            content = "Your submission has been rejected."

            # update db + email logic
            submission = SubmissionItem.objects.get(order_id=self.id) # get one record
            prev_status = submission['acceptance']
            submission.update(**self.json_data)
            cur_item = SubmissionItem.objects.get(order_id=self.id)

            if prev_status == cur_item['acceptance'] or cur_item['acceptance'] != 'rejected': # send rejection email only for the first time
                return 
            email_addr = cur_item['email']

        self.email.send_email(email_addr, subject, content)