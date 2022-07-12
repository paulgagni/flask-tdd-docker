from flask import Flask, jsonify
from flask_restx import Resource, Api

#Instantiate the app
app = Flask(__name__)
api = Api(app)

#Configure the first endpoint - Navigate to http://localhost:5000/ping in your browser and should see the message.
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

# Set config - This will pull in the development config from src/config.py
app.config.from_object('src.config.DevelopmentConfig')


#https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful/page/3
#The add_resource function registers the routes with the framework using the given endpoint.
api.add_resource(Ping, '/ping')