from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from models.fabricationitem import FabricationItem
from controllers.fabricationlifecycle import FabricationControl


class Fabrication(Resource):
    jlist = []
    # FabAPI = Api
    # fabEmail = EMAIL()

    def __init__(self, jlist=[]):
        self.jlist = jlist

    def get(self):
        self.jlist = []
        all_item = FabricationItem.objects()
        for record in all_item:
            self.jlist.append({
                "order_id": record['order_id'],
                "email": record['email'],
                "design": record['design'],
                "cost": record['cost'],
                "time": record['time'],
                "machinist": record['machinist'],
                "stage": record['stage']
            })
        return self.jlist

    def post(self):

        item = request.get_json()

        if not item:
            return {"message": "no input"}, 400
        
        process = FabricationControl(item)
        process.process_fabrication('fabAcc')
        process.process_fabrication('mac')

        return {"message": "success"}, 201

    def put(self):

        item = request.get_json()

        update_fabrication = FabricationItem.objects.get(order_id=item['order_id'])
        if not update_fabrication:
            return {"message": "item not found"}, 404
            
        process = FabricationControl(item)
        process.process_fabrication('comp')

        return {"message": "update success"}, 201

