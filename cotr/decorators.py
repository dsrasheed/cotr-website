from functools import wraps
from flask import session

def form_validation_required(form_name):
    """Add to views that process form data another view has validated. 
    This makes sure the form was successfully validated so no unsanitized
    form data is processed.

    :param form_name:
        The name of the form that was validated
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if session['form_validated'] != form_name:
                abort(403)
            session['form_validated'] = None
            return func()
        return inner
    return decorator

