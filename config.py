# Config classes

class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = 'Xb\xfc\xd7\xcbQE\x01D@\r\xd4\xb5N4\xa5.H\xe3\xfa\x1b7T-'

class Development(Config):
	DEBUG = True
