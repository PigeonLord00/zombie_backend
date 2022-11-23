import sqlite3

from flask_restful import Resource
from . import api


class FlagInfectedSurvivor(Resource):
    def put(self, name: str):

        db = sqlite3.connect('survivor.db')
        statement = ''' UPDATE survivors SET infected = 1 WHERE name = ?'''

        cursor = db.cursor()

        try:
            cursor.execute(statement, (name,))
            db.commit()
        except sqlite3.IntegrityError as error:
            return {'status': 'error', 'message': error.args}

        return {'status': 'success', 'message': f'{name} is now infected'}


api.add_resource(FlagInfectedSurvivor, '/flag-infected-survivor/<string:name>')
