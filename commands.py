from flask import Blueprint
from cv import cv_alex_oprinca
cv_blueprint = Blueprint('cli_command', __name__)

@cv_blueprint.cli.command('cv')
def education():
    print(cv_alex_oprinca)
