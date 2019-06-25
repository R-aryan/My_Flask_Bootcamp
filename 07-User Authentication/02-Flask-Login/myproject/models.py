
from myproject import db, login_manager
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model,UserMixin):

    __tablename__='users'

    id= db.Column(db.Integer,primary_key=True)
    email= db.Column(db.String(64),unique=True,index=True)
    username= db.Column(db.String(30),unique=True,index=True)
    full_name= db.Column(db.String(120))
    password_hash= db.Column(db.String(128))

    def __init__(self,email,un,fn,pwd):

        self.email=email
        self.username=un
        self.full_name=fn
        self.password_hash= generate_password_hash(pwd)

    def check_password(self,password):

        return check_password_hash(self.password_hash,password)
