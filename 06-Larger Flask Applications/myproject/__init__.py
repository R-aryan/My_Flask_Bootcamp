import os
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate ## pip install Flask-Migrate
#from flask_wtf import FlaskForm


app= Flask(__name__)

app.config['SECRET_KEY']= 'ritesharyan'

################################################
############## database configuration #########

basedir= os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

Migrate(app,db)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import  owner_blueprint

app.register_blueprint(owner_blueprint,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
#############################################################
