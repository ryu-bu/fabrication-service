from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from models.fabricationitem import FabricationItem
from controllers.fabricationlifecycle import FabricationControl
from models.submissionitem import SubmissionItem
from controllers.submissionlifescycle import SubmissionControl


class User(Resource):

    def get(self):
        sub_item = SubmissionItem.objects()
        fab_item = FabricationItem.objects()
        jlist = SubmissionControl.jsonize_items(sub_item) + FabricationControl.jsonize_items(fab_item)
        return jlist

    def post(self):

        item = request.get_json()

        if not item:
            return {"message": "no input"}, 400
        
        FabricationControl.usr_acc(item['order_id'], item['email'], item['design'], item['cost'], item['time'], item['machinist'], item['stage'])
        FabricationControl.mac_fab(item['order_id'])

        return {"message": "success"}, 201

    def put(self):

        item = request.get_json()
        
        return FabricationControl.usr_comp(item['order_id'], item['stage'])