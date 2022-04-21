from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, PasswordField , SelectField 
from wtforms.validators import DataRequired, Email, InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_sqlalchemy import SQLAlchemy 
 
class RegisterForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    location = StringField('Location', validators = [DataRequired()])
    biography = TextAreaField('Biography', validators = [DataRequired()])
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Please check format, only PNG and JPG images are allowed!")])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])



class AddCarForm(FlaskForm):
    make = StringField('Make', validators =[DataRequired()])
    colour = StringField('Colour', validators =[DataRequired()])
    price = StringField('Price', validators =[DataRequired()])
    transmission = SelectField('Transmission', choices =['Automatic', 'Manual'])
    model = StringField('Model', validators =[DataRequired()])
    year =  StringField('Year', validators =[DataRequired()])
    cartype = SelectField('Car Type', choices =['SUV', 'Sedan', 'Coupe', 'HatchBack', 'Wagon'])
    description =  TextAreaField('Description', validators = [DataRequired()]) 
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Please check format, only PNG and JPG images are allowed!")])