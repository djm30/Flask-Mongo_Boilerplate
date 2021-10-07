from flask import Flask
from flask_mongoengine import MongoEngine

dbName = 'AppData'

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "host" : f"mongodb://app_db/{dbName}"
}

db = MongoEngine(app)

from app import routes