
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,IntegerField
from wtforms.validators import email,EqualTo,DataRequired
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email= StringField('Enter email..!!',validators=[DataRequired(),email()])
    password= PasswordField('Enter your password:',validators=[DataRequired()])
    submit= SubmitField('Log In')


class Registrationform(FlaskForm):

    email= StringField('Enter your email id :',validators=[DataRequired(),email()])
    username= StringField('Enter Your Username:',validators=[DataRequired()])
    name= StringField('Enter your Full name:',validators=[DataRequired()])
    password= PasswordField('Enter password:',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must Match..!!')])
    pass_confirm= PasswordField('Re-enter to confirm:',validators=[DataRequired()])
    submit= SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered...!!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already taken....!!')
