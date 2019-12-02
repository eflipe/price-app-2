from flask import Blueprint

learning_blueprint = Blueprint('learning', __name__)


@learning_blueprint.route('/')
def home():
    return "Hola, mundo cruel"