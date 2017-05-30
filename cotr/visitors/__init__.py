from flask import Blueprint

visitors_blueprint = Blueprint(
    "visitors", __name__, 
    template_folder="templates"
)

from .views import *
