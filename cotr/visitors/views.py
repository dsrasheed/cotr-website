from flask import request
from . import visitors_blueprint

@visitors_blueprint.route("/get-tickets/success/", methods=["GET","POST"])
def success():
    retVal = ""
    for key, value in request.args:
        retVal += "{key}: {value}<br/>" % {
            "key": key,
            "value": value
        }

    for key, value in request.form:
        retVal += "{key}: {value}<br/>" % {
            "key": key,
            "value": value
        }

    return retVal
