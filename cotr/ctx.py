from flask import url_for
from . import app

@app.context_processor
def static_processor():
    def javascript(fn):
        return url_for('static', filename='js/' + fn + '.js')
    return dict(javascript=javascript)

