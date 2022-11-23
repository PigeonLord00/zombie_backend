from flask_restful import Resource
from . import api


class FlagInfectedSurvivor(Resource):
    def get(self, name: str):
        return {"message": f"Hello {name}"}


api.add_resource(FlagInfectedSurvivor, '/api/flag-infected-survivor/<string:name>')
