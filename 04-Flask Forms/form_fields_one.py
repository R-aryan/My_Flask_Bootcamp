from flask import Flask, render_template,request,session,redirect, url_for
from flask_wtf import FlaskForm
from wtforms import(StringField,BooleanField,DateTimeField,
                             RadioField,SelectField,TextField,SubmitField,TextAreaField)

from wtforms.validators import DataRequired

app= Flask(__name__)

app.config['SECRET_KEY']= 'mykey'

class InfoForm(FlaskForm):

    breed=StringField('What breed are you?',validators=[DataRequired()] )
    neutered= BooleanField("Have you been neutered ?  ")
    mood= RadioField("Please choose your mood:",
                    choices=[('mood_one','happy'),('mood_two','Excited')])

    food_choice= SelectField(u'Pick your Favourite Food:',
                             choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])

    feedback= TextAreaField()
    submit= SubmitField('submit')



@app.route('/',methods=['GET','POST'])
def index():

    form= InfoForm()
    if form.validate_on_submit():
        session['breed']= form.breed.data
        session['neutered']= form.neutered.data
        session['mood']= form.mood.data
        session['food_choice']= form.food_choice.data
        session['feedback']= form.feedback.data

        return redirect(url_for('thankyou'))
    
    return render_template('01-home.html',form=form)


@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html')

if __name__== '__main__':
    app.run(debug=True)

