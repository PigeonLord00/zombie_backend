from flask import url_for, redirect
from flask_restful import Resource
from . import api


class Root(Resource):
    def get(self):
        return {'message': 'Welcome to the api! Please see documentation for all requests'}


api.add_resource(Root, '/')
