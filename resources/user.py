from flask_restful import Resource
from flask import Flask, jsonify, request, Response
from models.fabricationitem import FabricationItem
from controllers.fabricationcontrol import FabricationControl
from models.submissionitem import SubmissionItem
from controllers.submissioncontrol import SubmissionControl
from controllers.usercontrol import UserControl
from flask_jwt_extended import jwt_required, get_jwt_identity


class User(Resource):

    # requires authentication
    @jwt_required

    def get(self):
        role = UserControl.get_role(get_jwt_identity())
        jlist = []
        if role == 'manager':
            sub_item = SubmissionItem.objects()
            jlist = SubmissionControl.jsonize_items(sub_item)

        fab_item = FabricationItem.objects()
        jlist = jlist + FabricationControl.jsonize_items(fab_item)

        return jlist

    def post(self):

        body = request.get_json()
        return UserControl.gen_user(body)

    def put(self):

        body = request.get_json()
        return UserControl.update_user(body)