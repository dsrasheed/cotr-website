from cotr.admin import admin_blueprint
from cotr.admin.models import Staff

@admin_blueprint.route('/login/', methods=['GET','POST'])
def login():
    pass

@admin_blueprint.route('/verify-ticket/', methods=['GET','POST'])
def verify_ticket():
    pass

