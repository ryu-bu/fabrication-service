from datetime import datetime
from mongoengine import *
from pytz import timezone

class SubmissionItem(Document):

    order_id = IntField(unique=True, required=True)
    email = EmailField(required=True)
    date = DateTimeField(default=datetime.now(timezone('US/Eastern')))
    acceptance = StringField(required=True)
    completion = StringField(required=True)
    time = IntField(required=True)
    cost = IntField(required=True)
    file = StringField(required=True)
    address = StringField(required=True)

    def toJson(self):
        in_json = {
            "order_id": self.order_id,
            "email": self.email,
            "date": self.date,
            "acceptance": self.acceptance,
            "completion": self.completion,
            "time": self.time,
            "cost": self.cost,
            "file": self.file,
            "address": self.addr,
        }

        return in_json
    
    meta = {
        "indexes": ["order_id", "email"],
        "ordering": ["date"]
    }