import click

from cotr import db, app
from cotr.admin.models import Staff

@app.cli.command()
@click.argument('username')
@click.argument('password')
def create_staff(username, password):
    s = Staff(username, password)
    db.session.add(s)
    print('Created staff member %s' % s)
    db.session.commit()

@app.cli.command()
@click.argument('filename')
def create_staff_from_file(filename):
    created_staff = []
    with open(filename, 'r') as f:
        for line in f:
            username, password = line.strip().split(':')
            s = Staff(username, password)
            db.session.add(s)
            created_staff.append(s)
    db.session.commit()

    for s in created_staff:
        print('Created: %s' % s)

@app.cli.command()
@click.argument('username')
def delete_staff(username):
    s = Staff.query.filter_by(username=username).first()
    if s is not None:
        db.session.delete(s)
        db.session.commit()
        print('Deleted: %s' % s)
    else:
        print('No staff member with username %s' % username)

@app.cli.command()
def view_staff():
    staff = Staff.query.all()
    for s in staff:
        print(s)
