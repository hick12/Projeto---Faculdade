from config import Config
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

mongodb_client = PyMongo(app, uri="mongodb+srv://palorca:e25331127@cluster0.gm8b8.mongodb.net/provamartins?retryWrites=true&w=majority")
db = mongodb_client.db

from app import routes