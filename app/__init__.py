

"""Instance of Flask application"""
# import os
from flask import Flask
from .api.v1 import blueprint_version1
# from config import app_config


def create_app(config_name):

    app = Flask(__name__)
    # app.config.from_object(app_config[config_name])
    app.register_blueprint(blueprint_version1, url_prefix='/api/v1')

    return app
