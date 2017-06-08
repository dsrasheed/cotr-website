from flask import request, current_app as app
import stripe

from . import visitors_blueprint

@visitors_blueprint.route('/buy/', methods=['POST'])
def buy():
    return 'Working'
