from flask import Flask
from flask.cli import FlaskGroup
from commands import cv_blueprint
from api import cv

def create_app(**kwargs):
    app = Flask(__name__, **kwargs)
    app.register_blueprint(cv_blueprint)
    app.register_blueprint(cv)
    return app

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()