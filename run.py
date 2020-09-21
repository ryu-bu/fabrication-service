from flask import Flask
from app import api_bp
from dotenv import load_dotenv
from mongoengine import *
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

load_dotenv()

connect("fab-service")


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix='/api')
    app.config.from_envvar('ENV_FILE_LOCATION')

    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    # from Model import db
    # db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)