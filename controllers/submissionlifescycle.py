from emailapi import Email
from models.submissionitem import SubmissionItem

class SubmissionControl:

    #sTEP 1 - save the data

    #step 2 - Do whaterever you need to do

    #Step 3 - send the notifications

    def jsonize_items(items):
        jlist = []
        for record in items:
            jlist.append({
                "order_id": record['order_id'],
                "email": record['email'],
                "acceptance": record['acceptance'],
                "completion": record['completion'],
                "time": record['time'],
                "cost": record['cost'],
                "file": record['file'],
                "address": record['address']
            }) # had to recreate this because all_item is not a mapping but string
        return jlist

    def usr_sub(json_data): # put json data directly to the method
        subject = "Submission Confirmation ID: " + str(json_data['order_id'])
        content = "Your record has been submitted successfully and will be reviewed shortly."

        # create new record on db
        submission = SubmissionItem(
            order_id = json_data['order_id'],
            email = json_data['email'],
            acceptance = json_data['acceptance'],
            completion = json_data['completion'],
            time = json_data['time'],
            cost = json_data['cost'],
            file = json_data['file'],
            address = json_data['address']
        )
        submission.save()
        Email().send_email(json_data['email'], subject, content)
        

    def mgr_sub(json_data):
        subject = "New Submission ID: " + str(json_data['order_id'])
        content = "New record has been submitted."
        email_addr = 'ryuichi1174@gmail.com'

        Email().send_email(email_addr, subject, content)
            
    def usr_rej(json_data):
        # update sub db command
        subject = "ID: " + str(json_data['order_id']) + " Rejected"
        content = "Your submission has been rejected."

        # update db + email logic
        submission = SubmissionItem.objects.get(order_id=json_data['order_id']) # get one record
        prev_status = submission['acceptance']
        submission.update(
            order_id = json_data['order_id'],
            acceptance = json_data['acceptance']
        )
        cur_item = SubmissionItem.objects.get(order_id=json_data['order_id'])

        if prev_status == cur_item['acceptance'] or cur_item['acceptance'] != 'rejected': # send rejection email only for the first time
            return 
        email_addr = cur_item['email']

        Email().send_email(email_addr, subject, content)