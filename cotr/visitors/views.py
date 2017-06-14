from flask import abort, request, session, url_for, \
                  current_app as app, abort, render_template
import stripe

from cotr import db, bcrypt
from cotr.visitors import visitors_blueprint
from cotr.decorators import form_validation_required
from cotr.visitors.models import Visitor, Ticket
from cotr.visitors.tasks import send_mail

_buy_tickets_msg = """
    Thank you for purchasing tickets to our event! <br />
    You can print your tickets whenever you would like simply
    by <a href="%s">clicking here</a>. <br />
    Don't delete this email if you would like to easily access
    your tickets for reprinting in the case that you lose them.
"""

def mail_ticket_print_url(email, token):
    msg = _buy_tickets_msg % (request.url_root + url_for('visitors.print', e=email, t=token))
    send_mail.delay(subject='Colors of the Region Event Tickets',
                    recipients=[email],
                    content=msg)

@visitors_blueprint.route('/buy/')
@form_validation_required('ticket')
def buy():
    data = session['form_data']
    email = data['email']
    quantity = data['quantity']

    returning_visitor = Visitor.query.filter_by(email=email).first()
    v = returning_visitor
    if returning_visitor is None:
        token = Visitor.get_token()
        mail_ticket_print_url(email, token)
        v = Visitor(email, token)
        db.session.add(v)

    # Loop and create multiple ticket objects.
    for x in range(quantity):
        t = Ticket(visitor=v)
        t.generate_barcode_img()
        db.session.add(t)
    
    # commit the db session
    db.session.commit()
    
    # Render a "success.html"
    return render_template('success.html')

@visitors_blueprint.route('/print/')
def print():
    email = request.args.get('e')
    token = request.args.get('t')

    v = Visitor.query.filter_by(email=email).first()
    if not v or not v.check_token(token):
        abort(403)
    
    tickets = Ticket.query.filter_by(visitor=v).all()
    return render_template('print.html', tickets=tickets)

