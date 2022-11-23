from flask_restful import Resource
from . import api


class UpdateSurvivorLocation(Resource):
    def get(self, name: str):
        return {"message": f"Hello {name}"}


api.add_resource(UpdateSurvivorLocation, '/api/update-survivor-location/<string:name>')
