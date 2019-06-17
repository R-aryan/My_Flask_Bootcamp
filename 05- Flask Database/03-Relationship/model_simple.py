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
    breed= db.Column(db.Text)
    age= db.Column(db.Integer)
    ## one to many relationship
    ## one puppy is connected to many toys
    toys= db.relationship('Toy',backref='puppy',lazy='dynamic')

    ### one to one relationship
    ### one Puppy ----- one Owner

    owner= db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    
    def __repr__(self):

        if self.owner:
            return f"Puppy name is {self.name} breed is {self.breed} age is {self.age} and the owner is {self.owner.name}"
        
        else:
            return f"Puppy name is {self.name} and it has no owner yet.....!!!"
    
    def report_toys(self):

        print(f"Here are toys of the puppy {self.name} : \n")
        
        for toy in self.toys:
            print(toy.item_name)
    



class Toy(db.Model):

    __tablename__= 'toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name= db.Column(db.Text)
    ##### Connecting the puppy table from puppy class to the toys table from toys class ####
    puppy_id= db.Column(db.Integer,db.ForeignKey('puppies.id'))


    def __init__(self,item_name,puppy_id):

        self.item_name= item_name
        self.puppy_id= puppy_id



class Owner(db.Model):
    
    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)

    ### now connecting the owners table with the puppies table of the class Puppy #####
    puppy_id= db.Column(db.Integer,db.ForeignKey('puppies.id'))


    def __init__(self,name,puppy_id):

        self.name= name
        self.puppy_id=puppy_id
    

