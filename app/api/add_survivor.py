from flask_restful import Resource, reqparse
from . import api
import sqlite3

reqparser = reqparse.RequestParser()
reqparser.add_argument('name', type=str)
reqparser.add_argument('age', type=str)
reqparser.add_argument('gender', type=str)
reqparser.add_argument('last_location', type=str)


class AddSurvivor(Resource):
    def post(self):
        arguments = reqparser.parse_args()
        print(arguments)

        db = sqlite3.connect('survivor.db')
        statement = ''' INSERT INTO survivors('name','age','gender','last_location')
                        VALUES(?,?,?,?)'''

        cursor = db.cursor()

        try:
            cursor.execute(statement, tuple(arguments.values()))
            db.commit()
        except sqlite3.IntegrityError as error:
            return {'status': 'error', 'message': error.args}

        return {'status': 'success', 'message': 'Survivor inserted successfully'}


api.add_resource(AddSurvivor, '/add-survivor')
