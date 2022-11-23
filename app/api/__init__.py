from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp)

from . import root
from . import add_survivor
from . import list_survivors
from . import update_survivor_location
from . import flag_infected
