import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '\xa4\xfdnu\xa6\xf5%?,\x99\x0eWT\x02\xccJ\x8bu\xfa-t\xbd\xeey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'getdown.db')
db = SQLAlchemy(app)

import views
import models