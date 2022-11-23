from flask_restful import Resource
from . import api


class ListSurvivors(Resource):
    def get(self, name: str):
        return {"message": f"Hello {name}"}


class ListSurvivor(Resource):
    def get(self, name: str):
        return {"message": f"Hello {name}"}


api.add_resource(ListSurvivors, '/api/all-survivors')
api.add_resource(ListSurvivor, '/api/all-survivors/<string:name>')
