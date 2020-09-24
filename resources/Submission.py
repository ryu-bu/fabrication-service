from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from controllers.submissioncontrol import SubmissionControl
from flask_jwt_extended import jwt_required

class Submit(Resource):

    def post(self):
        # db post function
        #STEP 1 - PARSE ALL THE DATA FROM JSON TO PYTHON VARIABLES
        #STEP 2 - CALL CORRESPONDING BUSINESS CLASSES/FUNCTIONS
        # somefunciton(data)

        item = request.get_json()

        if not item:
            return {"message": "no input"}
        
        SubmissionControl.usr_sub(item['order_id'], item['email'], item['acceptance'], item['completion'], item['time'], item['cost'], item['file'], item['address'])
        SubmissionControl.mgr_sub(item['order_id'])

        return {"message": "success"}, 201

    
class Submission(Resource):

    @jwt_required
    def get(self):

        arg = request.args
        order_id = arg['order_id']
        item = SubmissionControl.find_item(order_id)
        sub = SubmissionControl.jsonize_item(item)

        return sub

    @jwt_required
    def post(self):
        # db post function
        #STEP 1 - PARSE ALL THE DATA FROM JSON TO PYTHON VARIABLES
        #STEP 2 - CALL CORRESPONDING BUSINESS CLASSES/FUNCTIONS
        # somefunciton(data)

        item = request.get_json()

        if not item:
            return {"message": "no input"}
        
        SubmissionControl.usr_sub(item['order_id'], item['email'], item['acceptance'], item['completion'], item['time'], item['cost'], item['file'], item['address'])
        SubmissionControl.mgr_sub(item['order_id'])

        return {"message": "success"}, 201

    @jwt_required
    def put(self):
        # db put function
        item = request.get_json()
    
        return SubmissionControl.usr_rej(item['order_id'], item['acceptance'])

    @jwt_required
    def delete(self):

        item = request.get_json()

        return SubmissionControl.delete_item(item['order_id'])

