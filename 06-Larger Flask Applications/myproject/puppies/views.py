# myproject/owners/views.py

from flask import Blueprint,request,render_template,redirect,url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import Addform,Delform

puppies_blueprint= Blueprint('puppies',__name__,template_folder='templates/puppies')

@puppies_blueprint.route('/add',methods=['GET','POST'])
def add_pup():

    form=Addform()

    if form.validate_on_submit():

        name= form.name.data
        breed=form.breed.data
        age=form.age.data

        new_pup= Puppy(name,breed,age)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('add.html',form=form)


@puppies_blueprint.route('/list')
def list_pup():
    puppies=Puppy.query.all()
    return render_template('list.html',puppies=puppies)


@puppies_blueprint.route('/delete',methods=['GET','POST'])
def del_pup():

    form= Delform()

    if form.validate_on_submit():

        id= form.id.data
        pup= Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('delete.html',form=form)
