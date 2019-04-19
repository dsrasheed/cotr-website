import os

class Config(object):
    DEBUG =  False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
    STATIC_DIR = os.getenv('STATIC_DIR')

class Development(Config):
    DEBUG = True
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_TEST_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_TEST_KEY')

class Production(Config):
    pass

