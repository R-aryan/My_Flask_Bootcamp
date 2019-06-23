from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class Addowner(FlaskForm):
    name= StringField('Name of the owner :')
    pup_id= IntegerField('ID of the puppy :')
    submit=SubmitField('Add Owner')
