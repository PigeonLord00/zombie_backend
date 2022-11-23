from flask import Flask, Blueprint
from app.api import api_bp

app = Flask(__name__)

docs_bp = Blueprint('documentation', __name__, url_prefix='/documentation')

app.register_blueprint(api_bp)
app.register_blueprint(docs_bp)
