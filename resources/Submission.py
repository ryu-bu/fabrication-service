from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from Model import SubItem, Api
from Email import EMAIL


class Submission(Resource):
    
    jlist = []
    subAPI = Api
    subEmail = EMAIL()

    def get(self):
        return self.subAPI.get(self)

    def post(self):
        # db post function
        return self.subAPI.post(self, 'sub')

    def put(self):
        # db put function

        return self.subAPI.put(self)

