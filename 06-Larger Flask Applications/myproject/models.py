from myproject import db
# set up db in init.py file in myproject __file__
class Puppy(db.Model):

    __tablename__= 'puppies'#manual table name choice

    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.Text)
    breed= db.Column(db.Text)
    age= db.Column(db.Integer)
    owner=db.relationship('Owner',backref='puppy',uselist=False)


    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age

    def __repr__(self):

        if self.owner:

            return f"Puppy name is {self.name} breed is {self.breed} age is {self.age} year/s and the owner is {self.owner.name} \n"

        else:
            return f"Puppy name is {self.name} breed is {self.breed} age is {self.age} year/s and has no owner yet \n"




class Owner(db.Model):

    __tablename__= 'owners'
    id= db.Column(db.Integer,primary_key='True')
    name=db.Column(db.Text)
    puppy_id= db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id= puppy_id


    def __repr__(self):

        return f"owner name is : {self.name}"
