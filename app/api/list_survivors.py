import sqlite3

from flask_restful import Resource
from flask_restful_swagger import swagger

from . import api


class ListSurvivors(Resource):
    """Get all uninfected survivors in a list"""
    @swagger.operation(
        notes='An array with the details of all uninfected survivors will be returned'
    )
    def get(self):
        db = sqlite3.connect('survivor.db')
        statement = ''' SELECT * FROM survivors'''

        cursor = db.cursor()

        try:
            cursor.execute(statement)
            survivors = cursor.fetchall()
            response = {'status': 'success', 'survivors': []}
            for survivor in survivors:
                if not survivor[4]:
                    response['survivors'].append({
                        'name': survivor[0],
                        'age': survivor[1],
                        'gender': survivor[2],
                        'last_location': survivor[3],
                    })

        except sqlite3.IntegrityError as error:
            return {'status': 'error', 'message': error.args}

        return response


class ListSurvivor(Resource):
    """Get details of a specified survivor"""
    @swagger.operation(
        notes='Details of the survivors will be returned'
    )
    def get(self, name: str):
        db = sqlite3.connect('survivor.db')
        statement = ''' SELECT * FROM survivors WHERE name = ?'''
        cursor = db.cursor()

        try:
            cursor.execute(statement, (name,))
            survivor = cursor.fetchall()[0]
            if survivor[4]:
                return {'status': 'error', 'message': 'This person is no longer a survivor'}
            response = {'status': 'success', 'survivor': {
                'name': survivor[0],
                'age': survivor[1],
                'gender': survivor[2],
                'last_location': survivor[3],
            }}
        except sqlite3.IntegrityError as error:
            return {'status': 'error', 'message': error.args}

        return response


api.add_resource(ListSurvivors, '/all-survivors')
api.add_resource(ListSurvivor, '/all-survivors/<string:name>')
