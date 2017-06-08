import random
from string import ascii_lowercase, ascii_uppercase, digits

from cotr import db, bcrypt

class Visitor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    token = db.Column(db.String(60))
    tickets = db.relationship('Ticket', backref='visitor')

    def __init__(self, email, token=None):
        self.email = email
        
        token = token or self.get_token()
        self.token = bcrypt.generate_password_hash(token).decode('ascii')
    
    def get_token(self):
        characters = ascii_lowercase + ascii_uppercase + digits
        token = "".join([random.choice(characters) for x in range(25)])
        return token

    def __repr__(self):
        return "<Visitor %i: %s>" % (self.id, self.email)

class Ticket(db.Model):

    PRICE = 500

    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(13), unique=True)
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitor.id'))

    def __init__(self, barcode=None, visitor=None):
        self.barcode = barcode or self.get_barcode()
        self.visitor = visitor
    
    def get_barcode(self):
        barcode = "".join([random.choice(digits) for x in range(13)])
        return barcode

    def __repr__(self):
        return "<Ticket %i: %s>" % (self.id, self.barcode)

