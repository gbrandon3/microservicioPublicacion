from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask import request
from flask_restful import Resource
from datetime import datetime


class HealthCheck(Resource):
    def get(self):
        return "pong"
