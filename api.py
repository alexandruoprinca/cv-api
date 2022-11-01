from flask import jsonify, request, Blueprint
from http import HTTPStatus
from cv import cv_alex_oprinca

cv = Blueprint("cv_api", __name__)

@cv.route("/personal", methods=['GET'])
def personal():
    if(request.method == 'GET'):
        return jsonify({'data': cv_alex_oprinca.personal}), HTTPStatus.OK
    return jsonify(''), HTTPStatus.METHOD_NOT_ALLOWED

@cv.route("/experience", methods=['GET'])
def experience():
    if(request.method == 'GET'):
        return jsonify({'data': cv_alex_oprinca.experience}), HTTPStatus.OK
    return jsonify(''), HTTPStatus.METHOD_NOT_ALLOWED

@cv.route("/education", methods=['GET'])
def education():
    if(request.method == 'GET'):
        return jsonify({'data': cv_alex_oprinca.education}), HTTPStatus.OK
    return jsonify(''), HTTPStatus.METHOD_NOT_ALLOWED
