from flask import Flask,render_template,request,url_for,session,flash,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app= Flask(__name__)

app.config['SECRET_KEY']= 'ritesh-aryan'

class Simpleform(FlaskForm):

    submit= SubmitField('Click Me')


@app.route('/',methods=['GET','POST'])
def index():

    form= Simpleform()

    if form.validate_on_submit():
        flash('You just Clicked the Submit button...!!')

        return redirect(url_for('index'))
    
    return render_template('02-home.html',form=form)



if __name__== '__main__':
    app.run(debug=True)

