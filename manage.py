import sys

from flask.cli import FlaskGroup

from src import create_app, db   # new
from src.api.models import User  # new

#created a new FlaskGroup instance to extend the normal CLI with commands related to the Flask app.

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new

#registers a new command, recreate_db, to the CLI so that we can run it from the command line
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()