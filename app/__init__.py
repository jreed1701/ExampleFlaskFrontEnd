# -*- coding: utf-8 -*-
from app.api.views import api
from config import app_config, Config
from flask import Flask

def create_app(config_name):

    app = Flask(Config.APP_NAME, instance_relative_config=True)
    
    app.config.from_object(app_config[config_name])
                
    app.register_blueprint(api)
    
    return app