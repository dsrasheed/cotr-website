import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import stripe

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

from cotr.home import home_blueprint
from cotr.visitors import visitors_blueprint

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
	
    # Initialize third-party
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    stripe.api_key = app.config['STRIPE_SECRET_KEY']

    # Register blueprints
    app.register_blueprint(home_blueprint)
    app.register_blueprint(visitors_blueprint,
                           url_prefix='/tickets')

    return app
app = create_app('cotr.config.{}'.format(os.getenv('APP_SETTINGS')))

from cotr.ctx import *
from cotr.celery import app as celery_app
from cotr.visitors.models import *
