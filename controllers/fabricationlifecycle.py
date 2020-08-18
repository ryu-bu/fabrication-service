from emailapi import Email
from models.fabricationitem import FabricationItem

class FabricationControl:

    def jsonize_items(items):

        jlist = []
        
        for record in items:
            jlist.append({
                "order_id": record['order_id'],
                "email": record['email'],
                "design": record['design'],
                "cost": record['cost'],
                "time": record['time'],
                "machinist": record['machinist'],
                "stage": record['stage']
            })
        return jlist

    def usr_acc(json_data):
        # send acceptance email to the user
        subject = "ID: " + str(json_data['order_id']) + " Accepted"
        content = "Your submission has been accepted."

        # create new record on db
        fabrication = FabricationItem(
            order_id = json_data['order_id'],
            email = json_data['email'],
            design = json_data['design'],
            cost = json_data['cost'],
            time = json_data['time'],
            machinist = json_data['machinist'],
            stage = json_data['stage']
        )
        fabrication.save()
        email_addr = json_data['email']
        Email().send_email(email_addr, subject, content)

        # send job notication to machinist
    def mac_fab(json_data):
        subject = "New Request ID: " + str(json_data['order_id'])
        content = "New job has been requested."
        email_addr = 'ryuichi1174@gmail.com'

        Email().send_email(email_addr, subject, content)

        # when a record is updated
    def usr_comp(json_data):
        subject = "Order ID: " + str(json_data['order_id']) + " Completed"
        content = "Your order has been completed."

        # update db + email logic
        fabrication = FabricationItem.objects.get(order_id=json_data['order_id']) # get one record
        prev_status = fabrication['stage']
        fabrication.update(
            stage = json_data['stage']
        )
        cur_item = FabricationItem.objects.get(order_id=json_data['order_id'])

        if prev_status == cur_item['stage'] or cur_item['stage'] != 'completed': # send completion email only for the first time
            return
        email_addr = cur_item['email']
        
        Email().send_email(email_addr, subject, content)