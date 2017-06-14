from flask_wtforms import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Length, NumberRange, Required

class LoginForm(FlaskForm):
    
    username = StringField(u'Username' validators=[
        Required(u'You cannot leave this field blank')
    ])
    password = StringField(u'Password', validators=[
        Required(u'You cannot leave this field blank')
    ])

class TicketVerficationForm(FlaskForm):
    
    barcode = IntegerField(u'Barcode', validators=[
        Required(u'You cannot leave this field blank'),
        NumberRange(0, 9999999999999, u'The barcode you have entered is invalid')
    ])

