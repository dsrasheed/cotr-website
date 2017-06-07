import os

class Config(object):
    DEBUG =  False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

class Development(Config):
    DEBUG = True

class Production(Config):
    pass

