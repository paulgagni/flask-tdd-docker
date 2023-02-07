# manage.py

#configure the Flask CLI to run and manage the app from the command line
from flask.cli import FlaskGroup
from src import app

#creat FlaskGroup instance to extend the normal CLI with commands related to the Flask app
cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()