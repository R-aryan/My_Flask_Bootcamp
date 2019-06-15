import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir= os.path.abspath(os.path.dirname(__file__))

app= Flask(__name__)

####### Basic steps required for database connection ##############
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

#######################################################

class Puppy(db.Model):

    __tablename__= 'puppies'#manual table name choice

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)
    age= db.Column(db.Integer)


    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    def __repr__(self):

        return f"Puppy name is {self.name} and age is {self.age} year/s "
        
   

