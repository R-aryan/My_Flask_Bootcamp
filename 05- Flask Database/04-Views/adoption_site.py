
import os
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate ## pip install Flask-Migrate
#from flask_wtf import FlaskForm
from forms import Addform,Delform

app= Flask(__name__)

app.config['SECRET_KEY']= 'ritesharyan'

################################################
############## database configuration #########

basedir= os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)

Migrate(app,db)

######################################
######## Models #########



class Puppy(db.Model):

    __tablename__= 'puppies'#manual table name choice

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)
    breed= db.Column(db.Text)
    age= db.Column(db.Integer)

    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age

    def __repr__(self):


        return f"Puppy name is {self.name} breed is {self.breed} age is {self.age} year/s \n"


##################################################
######### Creating the actual view functions######

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():

    form=Addform()

    if form.validate_on_submit():

        name= form.name.data
        breed=form.breed.data
        age=form.age.data

        new_pup= Puppy(name,breed,age)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)

@app.route('/list')
def list_pup():

    puppies=Puppy.query.all()
    return render_template('list.html',puppies=puppies)



@app.route('/delete',methods=['GET','POST'])

def del_pup():

    form= Delform()

    if form.validate_on_submit():

        id= form.id.data
        pup= Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html',form=form)


if __name__=='__main__':
    app.run(debug='True')
