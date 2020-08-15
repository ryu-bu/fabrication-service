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
        return self.jlist

    def post(self):

        item = request.get_json()

        if not item:
            return {"message": "no input"}, 400

        self.jlist.append(item)
        
        process = FabricationControl(item)
        process.process_fabrication('fabAcc')
        process.process_fabrication('mac')

        return {"message": "success"}, 201

    def put(self):

        item = request.get_json()

        for record in self.jlist:
            if record['order_id'] == item['order_id']:
                for field in item:
                    if record[field] != item[field]:
                        record[field] = item[field]
                        if record[field] == 'completed':
                            process = FabricationControl(record)
                            process.process_fabrication('comp')
                
                return {"message": "update success"}, 201
                    
        return {"message": "item not found"}, 404

