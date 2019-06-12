from flask import Flask, render_template,request,session,redirect,flash,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app= Flask(__name__)

app.config['SECRET_KEY']= 'mykey'

class Simpleform(FlaskForm):

    breed= StringField('Enter the breed of the dog')
    submit= SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():

    form= Simpleform()

    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash(f"You just changed the breed to : {session['breed']}")

        return redirect((url_for('index')))
    
    return render_template('03-home.html',form=form)


if __name__== '__main__':
    app.run(debug=True)
