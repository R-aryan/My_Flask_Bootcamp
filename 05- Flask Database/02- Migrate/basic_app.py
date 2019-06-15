import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate ## pip install Flask-Migrate


basedir= os.path.abspath(os.path.dirname(__file__))

app= Flask(__name__)

####### Basic steps required for database connection ##############
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

Migrate(app,db)

######### linking the database with the app for migration ########

class Puppy(db.Model):
    
    __tablename__= 'puppies'#manual table name choice

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)
    age= db.Column(db.Integer)
    breed= db.Column(db.Text)


    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed

    
    def __repr__(self):

        return f"Puppy name is {self.name} and age is {self.age} year/s "
        