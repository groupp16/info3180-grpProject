from flask import Flask
<<<<<<< HEAD
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
=======
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
>>>>>>> cc11fd2d1f96cdb975e428e80672dced38ee3677
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

<<<<<<< HEAD
app.config.from_object(Config)
=======


# Instantiate Flask-Migrate library here

migrate = Migrate(app, db)
>>>>>>> cc11fd2d1f96cdb975e428e80672dced38ee3677
from app import views