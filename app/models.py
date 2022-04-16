# Add any model classes for Flask-SQLAlchemy here
from enum import unique
from . import db
from werkzeug.security import generate_password_hash
from datetime import datetime

class Car(db.Model):
    __tablename__ = 'Cars'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(1000))
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    colour = db.Column(db.String(50))
    year = db.Column(db.String(50))
    transmission = db.Column(db.String(50))
    car_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    photo = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, description, make, model, colour, year, transmission, car_type, price, photo, userid):
        self.description = description
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = userid

   

    
   
class Favourite(db.Model):

    __tablename__ = 'Favourites'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __init__(self, car_id, user_id):
        self.car_id = car_id
        self.user_id = user_id

   



    



class User(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(50), unique= True)
    name = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(50), unique= True)
    location = db.Column(db.String(50))
    biography = db.Column(db.String(1000))
    photo = db.Column(db.String(50), nullable=False)
    date_joined = db.Column(db.Datetime)

    def __init__(self, username, password, name, email, location, biography, photo, date_joined):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joined = date_joined

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
    
    def __repr__(self):
        return '<User %r>' % (self.username)

        






