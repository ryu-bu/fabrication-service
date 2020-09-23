from emailapi import Email
from models.submissionitem import SubmissionItem

class SubmissionControl:

    #sTEP 1 - save the data

    #step 2 - Do whaterever you need to do

    #Step 3 - send the notifications


    def jsonize_item(record):
        jitem = {
            "order_id": record['order_id'],
            "email": record['email'],
            "acceptance": record['acceptance'],
            "completion": record['completion'],
            "time": record['time'],
            "cost": record['cost'],
            "file": record['file'],
            "address": record['address']
        }

        return jitem

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

    def usr_sub(order_id, email, acceptance, completion, time, cost, file, address): # put json data directly to the method
        subject = "Submission Confirmation ID: " + str(order_id)
        content = "Your record has been submitted successfully and will be reviewed shortly."

        # create new record on db
        submission = SubmissionItem(
            order_id = order_id,
            email = email,
            acceptance = acceptance,
            completion = completion,
            time = time,
            cost = cost,
            file = file,
            address = address
        )
        submission.save()
        # Email().send_email(email, subject, content)


    def mgr_sub(order_id):
        subject = "New Submission ID: " + str(order_id)
        content = "New record has been submitted."
        email_addr = 'ryuichi1174@gmail.com'

        # Email().send_email(email_addr, subject, content)
            
    def usr_rej(order_id, acceptance):
        # update sub db command
        update_submission = SubmissionItem.objects.get(order_id=order_id)
        if not update_submission:
            return {"message": "item not found"}, 404

        subject = "ID: " + str(order_id) + " Rejected"
        content = "Your submission has been rejected."

        # update db + email logic
        submission = SubmissionItem.objects.get(order_id=order_id) # get one record
        prev_status = submission['acceptance']
        submission.update(
            order_id = order_id,
            acceptance = acceptance
        )
        cur_item = SubmissionItem.objects.get(order_id=order_id)

        if prev_status == cur_item['acceptance'] or cur_item['acceptance'] != 'rejected': # send rejection email only for the first time
            pass
        else:
            email_addr = cur_item['email']

            # Email().send_email(email_addr, subject, content)

        return {"message": "update success"}, 201

    def find_item(order_id):
        sub_record = SubmissionItem.objects.get(order_id=order_id)
        print(sub_record)

        return sub_record

    def delete_item(order_id):
        item = SubmissionItem.objects.get(order_id=order_id)
        item.delete()

        return {"message": "deletion success"}, 200