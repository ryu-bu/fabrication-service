import os

from flask import Flask, jsonify
from app import api_bp
from dotenv import load_dotenv
from mongoengine import *
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

load_dotenv()

connect("fab-service")


def echo(input_string: str) -> str:
    '''
    Simple call and response API Function
    '''
    return jsonify(
        {
            "Input String": f'{input_string}'
        }
    )


def placeholder_route() -> str:
    '''
    Placeholder for future user interface work.
    '''
    return "DAMPLAB Microfluidics Fabrication Service Coming Soon"


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.config.from_envvar('ENV_FILE_LOCATION')
    app.config['PROPAGATE_EXCEPTIONS'] = True

    bcrypt = Bcrypt(app)
    app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_BLACKLIST_ENABLED'] = True
    jwt = JWTManager(app)

    app.add_url_rule('/', view_func=placeholder_route)
    app.add_url_rule('/echo/<input_string>', view_func=echo)
    # from Model import db
    # db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=80)
