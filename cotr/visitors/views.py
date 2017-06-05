from flask import request
from . import visitors_blueprint

@visitors_blueprint.route("/buy/", methods=["POST"])
def buy():
    return "Working"
