import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from cotr.home import home_blueprint
from cotr.visitors import visitors_blueprint

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
	
    # Initialize third-party
    db.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(home_blueprint)
    app.register_blueprint(visitors_blueprint)

    return app
app = create_app('config.{}'.format(os.getenv('APP_SETTINGS')))

from cotr.ctx import *
