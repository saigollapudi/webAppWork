import os
from flask import Flask
from flask.ext.login import LoginManager
from config import basedir
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

# creation database 
db = SQLAlchemy(app) # creating a db object which represents our database

# creation of login manager
lm = LoginManager()
lm.init_app(app)

# to avoid circular references we wait till application is loaded
from app import views, models
