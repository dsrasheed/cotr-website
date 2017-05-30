from flask import request, render_template
from . import home_blueprint

@home_blueprint.route("/")
def index():
    return render_template("index.html")
