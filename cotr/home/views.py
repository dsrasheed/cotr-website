from flask import request, redirect, render_template, url_for, session
from werkzeug import ImmutableDict

from . import home_blueprint
from cotr.visitors.forms import TicketForm

# The index page contains multiple forms
index_forms = {
    'ticket': {
        'form_cls': TicketForm,
        'redirect': 'visitors.buy'
    }
}
index_forms = ImmutableDict(index_forms)

@home_blueprint.route('/', methods=['GET','POST'])
def index():
    ctx = {}
    form_name = None
    if request.method == 'POST':
        # Get the name of the form submitted
        form_name = request.args.get('f')

        # Get the class of the form that represents the data submitted
        form_cls = index_forms.get(form_name)['form_cls']
        
        # The user could have given a form_name that is not in index_forms
        if form_cls is not None:
            f = form_cls()
            if f.validate():
                session['validated_form'] = form_name
                session['form_data'] = f.data

                url = url_for(index_forms.get(form_name)['redirect'])
                return redirect(url)

            # Collect validation errors for the form since it is invalid
            ctx[form_name] = f

    # Add all the forms to the context for rendering
    for name in index_forms:
        # Add the form only if it has not already been added from the
        # the validation process
        if name != form_name:
            ctx[name] = index_forms[name]['form_cls']()
    return render_template('index.html', **ctx)

