import flask
from flask import Flask, Blueprint, request
from app.api import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp)


@app.route('/')
def welcome():
    return flask.render_template('welcome.html', url=f'{request.url}api/', docs=f'{request.url}api/spec')
