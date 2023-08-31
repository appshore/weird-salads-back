## Flask instance initialization

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_openapi3 import OpenAPI
from database import db

def create_app():
    app = OpenAPI(__name__)

    app.config.from_object('config')  # Load configuration from config.py

    db.init_app(app)

    return app