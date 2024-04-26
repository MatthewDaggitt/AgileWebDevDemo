from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)

from app import routes