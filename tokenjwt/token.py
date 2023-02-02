from flask_jwt_extended import create_access_token
from flask_restful import Resource
class Tokenjwt(Resource):
    def post(self):
        token = create_access_token(identity = 1)
        return token