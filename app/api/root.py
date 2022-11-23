from flask_restful import Resource
from . import api


class Root(Resource):
    def get(self):
        return {"message": "Hello World"}


api.add_resource(Root, '/')
