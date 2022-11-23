from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_autodoc.autodoc import Autodoc

app = Flask(__name__)
api = Api(app)
auto = Autodoc(app)


@auto.doc()
class Root(Resource):
    def get(self):
        return jsonify({"message": "Hello World"})


@auto.doc()
class SayHello(Resource):
    def get(self, name: str):
        return jsonify({"message": f"Hello {name}"})


api.add_resource(Root, '/api/')
api.add_resource(SayHello, '/api/hello/<string:name>')



@app.route('/documentation')
def documentation():
    return auto.html(template='zombiedocs.html',
                     title='ZSSN API Documentation',
                     author='Manjeet Singh',)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
