from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from controllers.submissionlifescycle import SubmissionControl
from models.submissionitem import SubmissionItem


class Submission(Resource):

    def get(self):
        
        all_item = SubmissionItem.objects()
        jlist = SubmissionControl.jsonize_items(all_item)
        return jlist

    def post(self):
        # db post function
        #STEP 1 - PARSE ALL THE DATA FROM JSON TO PYTHON VARIABLES
        #STEP 2 - CALL CORRESPONDING BUSINESS CLASSES/FUNCTIONS
        # somefunciton(data)

        item = request.get_json()

        if not item:
            return {"message": "no input"}
        
        SubmissionControl.usr_sub(item)
        SubmissionControl.mgr_sub(item)

        return {"message": "success"}, 201

    def put(self):
        # db put function
        item = request.get_json()

        update_submission = SubmissionItem.objects.get(order_id=item['order_id'])
        if not update_submission:
            return {"message": "item not found"}, 404

        SubmissionControl.usr_rej(item)
    
        return {"message": "update success"}, 201

