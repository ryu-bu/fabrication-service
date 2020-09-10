from emailapi import Email
from models.fabricationitem import FabricationItem

class FabricationControl:
    def jsonize_item(record):
        jitem = {
            "order_id": record['order_id'],
            "email": record['email'],
            "design": record['design'],
            "cost": record['cost'],
            "time": record['time'],
            "machinist": record['machinist'],
            "stage": record['stage']
        }

        return jitem

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

    def usr_acc(order_id, email, design, cost, time, machinist, stage):
        # send acceptance email to the user
        subject = "ID: " + str(order_id) + " Accepted"
        content = "Your submission has been accepted."

        # create new record on db
        fabrication = FabricationItem(
            order_id = order_id,
            email = email,
            design = design,
            cost = cost,
            time = time,
            machinist = machinist,
            stage = stage
        )
        fabrication.save()
        # Email().send_email(email, subject, content)

        # send job notication to machinist
    def mac_fab(order_id):
        subject = "New Request ID: " + str(order_id)
        content = "New job has been requested."
        email_addr = 'ryuichi1174@gmail.com'

        # Email().send_email(email_addr, subject, content)

        # when a record is updated
    def usr_comp(order_id, stage):
        update_fabrication = FabricationItem.objects.get(order_id=order_id)
        if not update_fabrication:
            return {"message": "item not found"}, 404

        subject = "Order ID: " + str(order_id) + " Completed"
        content = "Your order has been completed."

        # update db + email logic
        fabrication = FabricationItem.objects.get(order_id=order_id) # get one record
        prev_status = fabrication['stage']
        fabrication.update(
            stage = stage
        )
        cur_item = FabricationItem.objects.get(order_id=order_id)

        if prev_status == cur_item['stage'] or cur_item['stage'] != 'completed': # send completion email only for the first time
            pass
        else :
            email_addr = cur_item['email']
            # Email().send_email(email_addr, subject, content)
        
        return {"message": "update success"}, 201

    def find_item(order_id):
        fab_record = FabricationItem.objects.get(order_id=order_id)
        print(fab_record)

        return fab_record