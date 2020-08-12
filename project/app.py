from flask import Blueprint
from flask_restful import Api
from resources.Submission import Submission
from resources.Fabrication import Fabrication

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Submission, '/submission')
api.add_resource(Fabrication, '/fabrication')

