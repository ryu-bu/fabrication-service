from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from Model import FabItem, Api
from Email import EMAIL


class Fabrication(Resource):
    jlist = []
    FabAPI = Api
    fabEmail = EMAIL()

    def get(self):
        return self.FabAPI.get(self)

    def post(self):
        # if not request.get_json():
        #     return {'message': 'no input'}, 400
        
        # item = FabItem(**request.get_json())

        # # add to queue function here

        # self.jlist.append(item.toJson())
        # return {'message': 'success'}, 201
        return self.FabAPI.post(self, 'fab')

    def put(self):
        return self.FabAPI.put(self)

