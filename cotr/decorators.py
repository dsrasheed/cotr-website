from functools import wraps
from flask import session, abort

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
            form = session.get('validated_form')
            if form is None or form != form_name:
                abort(403)
            session['validated_form'] = None
            return func()
        return inner
    return decorator

