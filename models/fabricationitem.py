from datetime import datetime
from mongoengine import *
from pytz import timezone

class FabricationItem(Document):

    order_id = IntField(unique=True, required=True)
    email = EmailField(required=True)
    design = StringField(required=True)
    cost = IntField(required=True)
    time = IntField(required=True)
    machinist = StringField(required=True)
    stage = StringField(required=True)
    date = DateTimeField(default=datetime.now(timezone('US/Eastern')))

    def toJson(self):
        return {
            'order_id': self.id,
            'email': self.email,
            'design': self.design,
            'cost': self.cost,
            'time': self.time,
            'machinist': self.machinist,
            'stage': self.stage,
            'date': self.date
        }

    meta = {
        "indexes": ["order_id", "email"],
        "ordering": ["date"]
    }