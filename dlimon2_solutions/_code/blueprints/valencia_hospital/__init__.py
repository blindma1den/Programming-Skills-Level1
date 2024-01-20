from flask import Blueprint

valencia_hospital = Blueprint('valencia_hospital', __name__,
                        url_prefix='/valencia_hospital',
                        template_folder='templates')

from . import endpoints