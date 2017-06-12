from flask import abort, request, session, url_for, current_app as app
import stripe

from cotr import db
from cotr.visitors import visitors_blueprint
from cotr.decorators import form_validation_required
from cotr.visitors.models import Visitor, Ticket
from cotr.visitors.tasks import send_mail

_buy_tickets_msg = """
    Thank you for purchasing tickets to our event! <br />
    You can print your tickets whenever you would like simply
    by <a href=%s>clicking here</a>. <br />
    Don't delete this email if you would like to easily access
    your tickets for reprinting in the case that you lose them.
"""

def mail_ticket_print_url(email, token):
    msg = _buy_tickets_msg % url_for('visitors.print', e=email, t=token)
    send_mail.delay(subject='Colors of the Region Event Tickets',
                    recipients=[email],
                    content=msg)

@visitors_blueprint.route('/buy/')
@form_validation_required('ticket')
def buy():
    data = session['form_data']
    email = data['email']
    quantity = data['quantity']
    token = Visitor.get_token()
    
    mail_ticket_print_url(email, token)

    # Create a visitor object with email and token
    # The visitor object will hash the token.
    returning_visitor = Visitor.query.filter_by(email=email).first()
    v = returning_visitor
    if returning_visitor is None:
        v = Visitor(email, token)
        db.session.add(v)

    # Loop and create multiple ticket objects.
    for x in range(quantity):
        t = Ticket(visitor=v)
        db.session.add(t)
    
    # commit the db session
    db.session.commit()
    
    # Render a "success.html"
    return ", ".join([t.barcode for t in Ticket.query.filter_by(visitor=v).all()])

@visitors_blueprint.route('/print/')
def print():
    email = request.args.get('email')
    token = request.args.get('token')
    return "%s: %s" % (email, token)
