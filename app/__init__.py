from os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
loginmanager = LoginManager()
loginmanager.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views,models
