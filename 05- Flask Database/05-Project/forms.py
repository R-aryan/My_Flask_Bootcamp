
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class Addform(FlaskForm):

    name=StringField(' Enter Name of the Puppy :')
    breed= StringField(' Enter the breed of the puppy :')
    age= IntegerField(' Enter the age of the puppy :')
    submit=SubmitField('Add Puppy')


class Delform(FlaskForm):
    
    id= IntegerField('Enter the id of the puppy to remove')
    submit= SubmitField('Remove Puppy')

   
    
class Addowner(FlaskForm):
    name= StringField('Name of the owner :')
    pup_id= IntegerField('ID of the puppy :')
    submit=SubmitField('Add Owner')
    