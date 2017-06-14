from cotr import db, bcrypt

class Staff(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __init__(self, username=None, password=None):
        self.username = username
        
        if password is not None:
            self.set_password(password)

    def set_password(self, password):
        hashed = bcrypt.generate_password_hash(password).decode('ascii')
        self.password = hashed

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return '<Staff %i: %s>' % (self.id, self.username)
    
