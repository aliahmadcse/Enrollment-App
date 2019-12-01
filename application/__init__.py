from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Api


app = Flask(__name__)
# app configuration loading
app.config.from_object(Config)

# initializing api class
api = Api()
# providing app to the db object
api.init_app(app)

# instantiating the MongoEngine() class
db = MongoEngine()
# providing app to the db object
db.init_app(app)

from application import routes