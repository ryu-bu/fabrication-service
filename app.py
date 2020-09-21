from flask import Blueprint
from flask_restful import Api
from resources.submission import Submit, Submission
from resources.fabrication import Fabrication
from resources.user import User
from resources.loginapi import LoginAPI

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Submit, '/v1/submit')
api.add_resource(Submission, '/v1/submissionitem')
api.add_resource(User, '/v1/user')
api.add_resource(Fabrication, '/v1/fabricationitem') #return the selected item
api.add_resource(LoginAPI, '/v1/auth/login')

