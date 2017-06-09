from flask import abort, request, session, current_app as app
import stripe

from cotr.visitors import visitors_blueprint
from cotr.decorators import form_validation_required
from cotr.visitors.models import Visitor, Ticket


@visitors_blueprint.route('/buy/')
@form_validation_required('ticket')
def buy():
    data = session['form_data']
    email = data['email']
    quantity = data['quantity']
    
    token = Visitor.get_token()
    
