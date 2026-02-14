from flask import Blueprint

bp = Blueprint('books', __name__, url_prefix='/')

from . import views