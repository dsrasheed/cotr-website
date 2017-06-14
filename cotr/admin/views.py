from cotr.admin import admin_blueprint

@admin_blueprint.route('/login/', methods=['GET','POST'])
def login():
    pass

@admin_blueprint.route('/verify-ticket/', methods=['GET','POST'])
def verify_ticket():
    pass

