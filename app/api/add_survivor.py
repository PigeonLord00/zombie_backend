from flask_restful import Resource
from . import api


class AddSurvivor(Resource):
    def get(self):
        return {"message": "Hello World"}


api.add_resource(AddSurvivor, '/add-survivor')
