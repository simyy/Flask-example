#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
   
    # attack routes and cunstom err pages here
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
