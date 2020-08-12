from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from Model import SubItem, Api
from Email import EMAIL


class Submission(Resource):
    
    def __init__(self):
        self.jlist = []
        self.subAPI = Api
        self.subEmail = EMAIL()

    def get(self):
        return self.subAPI.get(self)

    def post(self):
        # db post function
        #STEP 1 - PARSE ALL THE DATA FROM JSON TO PYTHON VARIABLES
        #STEP 2 - CALL CORRESPONDING BUSINESS CLASSES/FUNCTIONS
        somefunciton(data)
        return self.subAPI.post(self, 'sub')

    def put(self):
        # db put function

        return self.subAPI.put(self)

