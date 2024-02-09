from flask import Blueprint

manchester_united = Blueprint('manchester_united', __name__,
                              url_prefix='/manchester_united',
                              template_folder='templates')

from . import endpoints