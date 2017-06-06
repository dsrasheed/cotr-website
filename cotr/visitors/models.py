import random
from string import ascii_lowercase, ascii_uppercase, digits
from cotr import db, bcrypt

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    token = db.Column(db.String(60))

    def __init__(self, email, token=None):
        self.email = email
        if token is None:
            token = self.get_token()
        self.token = bcrypt.generate_password_hash(token).decode('ascii')
    
    def get_token(self):
        characters = ascii_lowercase + ascii_uppercase + digits
        token = "".join([random.choice(characters) for x in range(25)])
        return token

    def __repr__(self):
        return "<Visitor %s>" % self.email

