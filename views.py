"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from crypt import methods
import os
import jwt
from app import app
from flask import json,render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from app.forms import  RegisterForm, LoginForm, AddCarForm
from datetime import datetime
from app.models import *
from flask _wtf.csrf import  generate_csrf


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/register', methods=['POST'])
def register():
    form = RegisterForm()
    current_dt = datetime.now()
    if form.validate_on_submit():
        image = form.photo.data
        filename = secure_filename(image.filename)
        user = Users(username = form.username.data, password = form.password.data, name = form.name.data,
        email = form.email.data, location = form.location.data, biography = form.biography.data,
        photo = filename, date_joined = current_dt.strftime("%Y-%m-%d " + "%X"))
        db.session.add(user)
        db.session.commit()
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return json.jsonify(username = form.username.data, name = form.name.data, photo = filename,
        email = form.email.data, location = form.location.data, biography = form.biography.data,
        date_joined = current_dt.strftime("%Y-%m-%d " + "%X"))

@app.route('/api/auth/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data:
            username = form.username.data
            password = form.password.data
            user = Users.query.filter_by(username=username).first()
            if user is not None and check_password_hash(user.password, password):
            # get user id, load into session
                login_user(user)    
                payload = {
                    'username': username,
                    'password': password
                }
                token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
                return json.jsonify(status=200, token = token)@app.route('/api/auth/login', methods=['POST'])

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return json.jsonify(status=200)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})



@app.route('/api/cars', methods= ['POST'])
def cars():
    form = AddCarForm()
    if form.validate_on_submit():
        pr = float(form.price.data)
        image = form.photo.data
        filename = secure_filename(image.filename)
        car = Car(description= form.description.data, make = form.make.data, model= form.model.data, colour= form.colour.data,
        year= form.year.data, transmission= form.transmission.choices, car_type= form.cartype.choices, price= pr, photo = filename  )
        db.session.add(car)
        db.session.commit()
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return json.jsonify(description= form.description.data, make = form.make.data, model= form.model.data, colour= form.colour.data,
        year= form.year.data, transmission= form.transmission.data, car_type= form.cartype.data, price= pr, photo = filename  )


    

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")