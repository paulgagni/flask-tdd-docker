# src/__init__.py
import os
#configure first endpoint
from flask import Flask, jsonify
from flask_restx import Resource, Api



# instantiate the app
app = Flask(__name__)

api = Api(app)

#Set Config from config.py
#app.config.from_object('src.config.DevelopmentConfig')
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


#print(app.config, file=sys.stderr)

api.add_resource(Ping, '/ping')