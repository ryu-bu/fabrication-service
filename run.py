from flask import Flask
from app import api_bp
from mongoengine import *
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from models.useritem import UserItem
from dotenv import load_dotenv, find_dotenv
from controllers.usercontrol import UserControl as user
import os
load_dotenv(find_dotenv())


connect("fab-service")


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp, url_prefix='/api')
    app.config.from_envvar('ENV_FILE_LOCATION')

    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    man = UserItem.objects(email=os.getenv('ADMINMAN'))
    if not man:
        print('manager does not exist...')
        print('adding manager')
        body = {
            "email": os.getenv('ADMINMAN'),
            "password": os.getenv('ADMINPASS')
        }
        print(user.gen_manager(body))
        print('manager added')

    # from Model import db
    # db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)