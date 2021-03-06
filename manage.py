from flask.cli import FlaskGroup
from src import app, db

#created a new FlaskGroup instance to extend the normal CLI with commands related to the Flask app.
cli = FlaskGroup(app)

#registers a new command, recreate_db, to the CLI so that we can run it from the command line
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()