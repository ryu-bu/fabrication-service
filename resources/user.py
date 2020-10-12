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
        fab_item = FabricationItem.objects()
        if role == 'manager':
            sub_item = SubmissionItem.objects()
            jlist = SubmissionControl.jsonize_items(sub_item) + FabricationControl.jsonize_items(fab_item)

        else: # only returns items associated with the machinist email
            email = UserControl.get_email(get_jwt_identity())
            print(fab_item)
            for item in fab_item:
                print(item.machinist)
                if item.machinist == email:
                    jlist.append(FabricationControl.jsonize_item(item))
                    

        return jlist

    def post(self):

        body = request.get_json()
        return UserControl.gen_user(body)

    def put(self):

        body = request.get_json()
        return UserControl.update_user(body)