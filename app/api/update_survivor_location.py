import sqlite3

from flask_restful import Resource, reqparse
from . import api

reqparser = reqparse.RequestParser()
reqparser.add_argument('last_location', type=str)

class UpdateSurvivorLocation(Resource):
    def put(self, name: str):
        arguments = reqparser.parse_args()
        print(arguments)

        db = sqlite3.connect('survivor.db')
        statement = ''' UPDATE survivors SET last_location = ? WHERE name = ?'''

        cursor = db.cursor()

        try:
            cursor.execute(statement, (arguments['last_location'], name))
            db.commit()
        except sqlite3.IntegrityError as error:
            return {'status': 'error', 'message': error.args}

        return {'status': 'success', 'message': 'Survivor location updated successfully'}


api.add_resource(UpdateSurvivorLocation, '/update-survivor-location/<string:name>')
