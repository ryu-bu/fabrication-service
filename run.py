from flask import Flask
from app import api_bp
from dotenv import load_dotenv
from mongoengine import *

load_dotenv()

connect("fab-submission")


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(api_bp, url_prefix='/api')

    # from Model import db
    # db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)