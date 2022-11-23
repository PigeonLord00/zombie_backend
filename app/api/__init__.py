from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = swagger.docs(Api(api_bp), apiVersion='1', api_spec_url="/spec")

from . import root
from . import add_survivor
from . import list_survivors
from . import update_survivor_location
from . import flag_infected
