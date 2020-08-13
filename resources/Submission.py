from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from model.submissionitem import SubmissionItem
from control.submissionlifescycle import SubmissionControl


class Submission(Resource):
    
    def __init__(self, jlist=[]):
        self.jlist = jlist
        # self.subAPI = Api
        # self.subEmail = EMAIL()

    def get(self):
        return self.jlist

    def post(self):
        # db post function
        #STEP 1 - PARSE ALL THE DATA FROM JSON TO PYTHON VARIABLES
        #STEP 2 - CALL CORRESPONDING BUSINESS CLASSES/FUNCTIONS
        # somefunciton(data)

        if not request.get_json():
            return {"message": "no input"}

        item = SubmissionItem(**request.get_json())
        self.jlist.append(item.toJson())

        process = SubmissionControl(item.toJson())
        process.ProcessSubmission('sub')
        process.ProcessSubmission('man')

        return {"message": "success"}, 201

    def put(self):
        # db put function
        item = request.get_json()

        for record in self.jlist:
            if record['id'] == item['id']:
                for field in item:
                    if record[field] != item[field]:
                        record[field] = item[field]
                        if record[field] == 'rejected':
                            process = SubmissionControl(record)
                            process.ProcessSubmission('fabRej')

                return {"message": "update success"}, 201
        
        return {"message": "item not found"}, 404

