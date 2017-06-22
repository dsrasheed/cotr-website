from functools import wraps

from flask import request, render_template, session, abort, redirect, url_for

from cotr.admin import admin_blueprint
from cotr.admin.models import Staff
from cotr.admin.forms import LoginForm, TicketVerificationForm
from cotr.visitors.models import Ticket
from cotr import db

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if session.get('logged_in') == True:
            return f(*args, **kwargs)
        abort(403)
    return inner

def authenticate_staff(username, password):
    s = Staff.query.filter_by(username=username).first()
    if s is not None:
        return s if s.check_password(password) else None

@admin_blueprint.route('/login/', methods=['GET','POST'])
def login():
    f = LoginForm()
    if f.validate_on_submit():
        username = f.data['username']
        password = f.data['password']
        staff = authenticate_staff(username, password)
        
        if staff is not None:
            # No staff member holds privileges over other
            # staff, so no need to distinguish between
            # them, just need to know if a user is one.
            session['logged_in'] = True
            return redirect(url_for('admin.verify_ticket'))
    return render_template('login.html', form=f)
        
@admin_blueprint.route('/logout/')
@login_required
def logout():
    session['logged_in'] = False
    return redirect(url_for('home.index'))

@admin_blueprint.route('/verify-ticket/', methods=['GET','POST'])
@login_required
def verify_ticket():
    f = TicketVerificationForm()
    is_verified = False
    has_entered = False
    if f.validate_on_submit():
        barcode = str(f.data['barcode'])
        # filter for barcode, if you get a match then set a variable that says that
        # if there was a ticket that was returned, check if has_entered is True,
        # if it is, set a variable that also tells us that in the template.
        t = Ticket.query.filter_by(barcode=barcode).first()
        if t is not None:
            is_verified = True

            # Making sure a ticket cannot be used to allow multiple people to enter.
            # Template displays a message to not allow the visitor in if has_entered
            # is True.
            has_entered = t.has_entered
            if not t.has_entered:
                t.has_entered = True
                db.session.add(t)
                db.session.commit()
    return render_template('verify_ticket.html', form=f,
        is_verified=is_verified, has_entered=has_entered)

