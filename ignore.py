from flask import Flask, request, Response
from emailapi import EMAIL

class SubmissionItem: 
    id = ""
    username = ""
    email = ""
    date = ""
    acceptance = ""
    completion = ""
    time = ""
    cost = ""
    file = ""

    def __init__(self, id, username, email, date, acceptance, completion, time, cost, file):
        self.id = id
        self.username = username
        self.email = email
        self.date = date
        self.acceptance = acceptance
        self.completion = completion
        self.time = time
        self.cost = cost
        self.file = file

    def toJson(self):
        in_json = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "date": self.date,
            "acceptance": self.acceptance,
            "completion": self.completion,
            "time": self.time,
            "cost": self.cost,
            "file": self.file,
        }

        return in_json

    def toJson2(self):
        return self.__dict__


class FabItem:
    id = ""
    design = ""
    cost = ""
    time = ""
    machinist = ""
    stage = ""

    def __init__(self, id, design, cost, time, machinist, stage):
        self.id = id
        self.design = design
        self.cost = cost
        self.time = time
        self.machinist = machinist
        self.stage = stage

    def toJson(self):
        return {
            'id': self.id,
            'design': self.design,
            'cost': self.cost,
            'time': self.time,
            'machinist': self.machinist,
            'stage': self.stage
        }


class Api:

    def get(self):
        return self.jlist
    
    def post(self, type):
        if not request.get_json():
            return {"message": "no input"}, 400

        if (type == 'sub'):
            item = SubmissionItem(**request.get_json())
            self.subEmail.send_email('ryu74@bu.edu', 'sub', item.id)
            self.subEmail.send_email('ryu74@bu.edu', 'man', item.id)
        else:
            item = FabItem(**request.get_json())
            self.fabEmail.send_email('ryu74@bu.edu', 'fabAcc', item.id)
            self.fabEmail.send_email('ryu74@bu.edu', 'mac', item.id)
        
        self.jlist.append(item.toJson())
        return {"message": "success"}, 201

    def put(self):
        item = request.get_json()

        for record in self.jlist:
            if record['id'] == item['id']:
                for field in item:
                    record[field] = item[field]
                    if record[field] == 'rejected':
                        self.subEmail.send_email('ryu74@bu.edu', 'fabRej', item['id'])
                    if record[field] == 'completed':
                        self.fabEmail.send_email('ryu74@bu.edu', 'comp', item['id'])

                return {"message": "update success"}, 201

        return {"message": "item not found"}, 404