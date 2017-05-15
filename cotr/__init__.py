import os
from flask import Flask

def create_app(config_object):
	app = Flask(__name__)
	app.config.from_object(config_object)
	
	return app

app = create_app('config.{}'.format(os.getenv('APP_SETTINGS')))

from cotr.views import *
