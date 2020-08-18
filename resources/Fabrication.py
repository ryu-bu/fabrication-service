from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from models.fabricationitem import FabricationItem
from controllers.fabricationlifecycle import FabricationControl


class Fabrication(Resource):

    def get(self):
        
        all_item = FabricationItem.objects()
        jlist = FabricationControl.jsonize_items(all_item)
        return jlist

    def post(self):

        item = request.get_json()

        if not item:
            return {"message": "no input"}, 400
        
        FabricationControl.usr_acc(item)
        FabricationControl.mac_fab(item)

        return {"message": "success"}, 201

    def put(self):

        item = request.get_json()

        update_fabrication = FabricationItem.objects.get(order_id=item['order_id'])
        if not update_fabrication:
            return {"message": "item not found"}, 404
            
        FabricationControl.usr_comp(item)

        return {"message": "update success"}, 201

