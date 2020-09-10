from flask import Blueprint
from flask_restful import Api
from resources.submission import Submission
from resources.fabrication import FabricationList, Fabrication
from resources.user import User

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Submission, '/v1/submissionitem')
api.add_resource(User, '/v1/user')
api.add_resource(FabricationList, '/v1/fabricationitem')
api.add_resource(Fabrication, '/v1/fabricationitem?order_id=<int:order_id>')

