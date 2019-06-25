from myproject import app,db
from flask import Flask
from flask import render_template,url_for,redirect,request,abort,flash
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm,Registrationform
from werkzeug.security import check_password_hash,generate_password_hash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():

    logout_user()
    flash("You logged out from the page...!!!")
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():

    form= LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email= form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Sucessfully...!!!")

            next= request.args.get('next')

            if next==None or not next[0]=='/':
                next= url_for('welcome_user')

            return redirect(next)

    return render_template('login.html',form=form)


@app.route('/register',methods=['GET','POST'])
def register():

    form= Registrationform()

    if form.validate_on_submit():
        email= form.email.data
        username= form.username.data
        name= form.name.data
        password= form.password.data

        user = User(email,username,name,password)
        db.session.add(user)
        db.session.commit()

        flash("Thanks for registration..!!")
        return redirect(url_for('login'))

    return render_template('register.html',form=form)



if __name__=='__main__':
    app.run(debug='True')
