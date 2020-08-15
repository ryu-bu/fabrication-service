from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from controllers.submissionlifescycle import SubmissionControl
from models.submissionitem import SubmissionItem


class Submission(Resource):
    
    def __init__(self, jlist=[]):
        self.jlist = jlist
        # self.subAPI = Api
        # self.subEmail = EMAIL()

    def get(self):
        self.jlist = []
        all_item = SubmissionItem.objects()
        for record in all_item:
            self.jlist.append({
                "order_id": record['order_id'],
                "email": record['email'],
                "acceptance": record['acceptance'],
                "completion": record['completion'],
                "time": record['time'],
                "cost": record['cost'],
                "file": record['file'],
                "address": record['address']
            })
        return self.jlist

    def post(self):
        # db post function
        #STEP 1 - PARSE ALL THE DATA FROM JSON TO PYTHON VARIABLES
        #STEP 2 - CALL CORRESPONDING BUSINESS CLASSES/FUNCTIONS
        # somefunciton(data)

        item = request.get_json()

        if not item:
            return {"message": "no input"}
        
        # material.save()
        process = SubmissionControl(item)
        process.process_submission('sub')
        process.process_submission('man')

        return {"message": "success"}, 201

    def put(self):
        # db put function
        item = request.get_json()

        update_submission = SubmissionItem.objects.get(order_id=item['order_id'])
        if not update_submission:
            return {"message": "item not found"}, 404

        process = SubmissionControl(item)
        process.process_submission('fabRej')
    
        return {"message": "update success"}, 201

        # for record in self.jlist:
        #     if record['order_id'] == item['order_id']:
        #         for field in item:
        #             if record[field] != item[field]:
        #                 record[field] = item[field]
        #                 if record[field] == 'rejected':
        #                     print(record['email'])
        #                     process = SubmissionControl(record)
        #                     process.process_submission('fabRej')

        #         return {"message": "update success"}, 201
        
        # return {"message": "item not found"}, 404

