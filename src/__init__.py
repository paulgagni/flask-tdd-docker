import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

#Instantiate the app
app = Flask(__name__)
api = Api(app)


# Set config - This will pull in the development config from src/config.py
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

#Instantiate the database
db = SQLAlchemy(app)

#Define the database model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


#Test proper config was loaded
#print(app.config, file=sys.stderr)

#Configure the first endpoint - Navigate to http://localhost:5000/ping in your browser and should see the message.
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

#https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful/page/3
#The add_resource function registers the routes with the framework using the given endpoint.
api.add_resource(Ping, '/ping')