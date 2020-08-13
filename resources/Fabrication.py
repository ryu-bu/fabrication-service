from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from model.fabricationitem import FabricationItem
from control.fabricationlifecycle import FabricationControl


class Fabrication(Resource):
    jlist = []
    # FabAPI = Api
    # fabEmail = EMAIL()

    def __init__(self, jlist=[]):
        self.jlist = jlist

    def get(self):
        return self.jlist

    def post(self):
        if not request.get_json():
            return {"message": "no input"}, 400

        item = FabricationItem(**request.get_json())
        self.jlist.append(item.toJson())
        
        process = FabricationControl(item.toJson())
        process.ProcessFabrication('fabAcc')
        process.ProcessFabrication('mac')

        return {"message": "success"}, 201

    def put(self):

        item = request.get_json()

        for record in self.jlist:
            if record['id'] == item['id']:
                for field in item:
                    if record[field] != item[field]:
                        record[field] = item[field]
                        if record[field] == 'completed':
                            process = FabricationControl(record)
                            process.ProcessFabrication('comp')
                
                return {"message": "update success"}, 201
                    
        return {"message": "item not found"}, 404

