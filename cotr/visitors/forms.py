from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField
from wtforms.validators import Email, Length, NumberRange, Required, ValidationError
import stripe

from .models import Ticket

def validate_token_with_charge(form, field):
    # To make a charge, we need to know how many tickets
    # the visitor wants to buy.
    if len(form.quantity.errors) != 0:
        return

    charge_token = field.data
    quantity = form.quantity.data
    try:
        charge = stripe.Charge.create(
            amount=Ticket.PRICE * quantity,
            currency='usd',
            description='Purchasing tickets',
            source=charge_token
        )
        if not charge.paid:
            raise Exception()
    except Exception as e:
        # body = e.json_body
        # err = body['error']
        # raise ValidationError(err['message'])
        raise ValidationError('Something went wrong while \
            processing your credit card information')
        
class TicketForm(FlaskForm):

    email = StringField(u'Email Address', validators=[
        Required(u'You must specify an email.'),
        Email(u'The email provided is not valid.'),
    ])
    quantity = IntegerField('Quantity', validators=[
        Required(u'You must specify the quantity of tickets to buy'),
        NumberRange(1, 20, u'You can only buy between 1-20 tickets')
    ])
    stripeToken = HiddenField(validators=[Required(), validate_token_with_charge])

