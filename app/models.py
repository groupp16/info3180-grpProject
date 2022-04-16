from . import db
from werkzeug.security import generate_password_hash

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    password=db.Column(db.String(255))
    name=db.Column(db.String(255)) 
    email=db.Column(db.String(255)) 
    location=db.Column(db.String(255)) 
    biography=db.Column(db.String(255)) 
    photo=db.Column(db.String(255))
    date_joined=db.Column(db.String(255))

    def __init__(self, username, password,name, email, location, biography, photo, date_joined):
        self.username=username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.name=name
        self.email=email
        self.location=location 
        self.biography=biography
        self.photo=photo
        self.date_joined=date_joined

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support