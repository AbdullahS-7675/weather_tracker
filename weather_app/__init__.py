from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from weather_app.routes import main
    app.register_blueprint(main)

    return app