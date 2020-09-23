from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from models.fabricationitem import FabricationItem
from controllers.fabricationcontrol import FabricationControl


# class FabricationList(Resource):

#     def get(self):

#         all_item = FabricationItem.objects()
#         jlist = FabricationControl.jsonize_items(all_item)
#         return jlist

#     def post(self):

#         item = request.get_json()

#         if not item:
#             return {"message": "no input"}, 400
        
#         FabricationControl.usr_acc(item['order_id'], item['email'], item['design'], item['cost'], item['time'], item['machinist'], item['stage'])
#         FabricationControl.mac_fab(item['order_id'])

#         return {"message": "success"}, 201

#     def put(self):

#         item = request.get_json()
        
#         return FabricationControl.usr_comp(item['order_id'], item['stage'])

class Fabrication(Resource):
     
    def get(self):

        arg = request.args
        order_id = arg['order_id']
        item = FabricationControl.find_item(order_id)
        fab = FabricationControl.jsonize_item(item)

        return fab

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

    def delete(self):

        item = request.get_json()

        return FabricationControl.delete_item(item['order_id'])


        
    
    

