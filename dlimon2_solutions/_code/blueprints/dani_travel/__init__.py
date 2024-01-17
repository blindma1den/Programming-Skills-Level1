from flask import Blueprint

dani_travel = Blueprint('dani_travel', __name__,
                        url_prefix='/dani_travel',
                        template_folder='templates')

from . import endpoints