"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""


from app import app,db,login_manager
from flask import render_template, request, jsonify, send_file,g, make_response,redirect, url_for,flash,send_from_directory
from flask import request
import os
from app.models import *
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from app.forms import *
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, current_user, login_required

# Using JWT
import jwt
from flask import _request_ctx_stack
from functools import wraps
import datetime

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = "Bearer "+ request.cookies.get('token', None) 

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer','token':parts[0]}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated


def generate_token(id,name):
    payload = {
        'sub': id, # subject, usually a unique identifier
        'name': name
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    return token


@app.route('/api/register', methods=['POST'])
def register():
    form = RegisterForm()
   
    if request.method == 'POST' and form.validate_on_submit():
        current_dt = datetime.datetime.now()
        image = form.photo.data
        filename = secure_filename(image.filename)
        
        username = form.username.data 
        password = form.password.data 
        name = form.fullname.data
        email = form.email.data 
        location = form.location.data
        biography = form.biography.data
        photo = filename
        date_joined = current_dt.strftime("%Y-%m-%d " + "%X")

        user_info = Users(username,password,name,email,location,biography,photo,date_joined)
        db.session.add(user_info)
        db.session.commit()
        
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(username = username, name = name, photo = filename,
        email = email, location = location, biography = biography,date_joined = date_joined)

@app.route('/api/auth/login', methods=['POST'])
def login():
    form = LoginForm()
   
    if form.validate_on_submit() and request.method == 'POST':
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(username=username).first()
        
        if user is not None and check_password_hash(user.password, password):

                login_user(user)    
                token=generate_token(user.id,user.name)
                resp = make_response(jsonify(error=None, data={'token': "Bearer " +token}, message="Token Generated"))
                resp.set_cookie('token', token, httponly=True, secure=True)
                return resp
        return jsonify(error="Error in login")        

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify(status=200)

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/cars', methods=['POST','GET'])
@login_required
@requires_auth
def explore():
    # Form data
    if current_user.is_authenticated:
       
        form = AddCarForm()

        # Validate file upload on submit
        if request.method == 'POST' and form.validate_on_submit():
            # Get file data and save to your uploads folder
            
            pr = float(form.price.data)
            image = form.photo.data
            filename = secure_filename(image.filename)

            description= form.description.data
            make = form.make.data
            model= form.model.data
            colour= form.colour.data
            year= form.year.data
            transmission= request.form['transmission']
            car_type= request.form['cartype']
            price= pr
            photo = filename
            user_id=current_user.get_id()
            car = Cars(description, make, model, colour,year, transmission, car_type, price, photo,user_id)
            db.session.add(car)
            db.session.commit()
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            return jsonify(description= description, make = make, model= model, colour= colour,
            year= year, transmission= transmission, car_type= car_type, price= pr, photo = filename,user_id=user_id )
        
        if request.method == 'GET':           
            return jsonify(cars=[i.serialize() for i in  db.session.query(Cars).order_by(Cars.id.desc()).limit(3)])
            
@app.route('/api/search', methods=['GET'])
@login_required
@requires_auth
def search():
    if current_user.is_authenticated:
        args = request.args
        make=args.get("make")
        model=args.get("model")

        # [i.serialize() for i in  Cars.query.filter_by(make=make).order_by(Cars.id.desc()).limit(3)]
        return jsonify(cars=make)
            











@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))





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