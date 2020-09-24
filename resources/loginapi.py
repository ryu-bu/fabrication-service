from flask import Response, request
from controllers.usercontrol import UserControl
from flask_restful import Resource


class LoginAPI(Resource):
    def post(self):
        body = request.get_json()
        return UserControl.get_token(body)