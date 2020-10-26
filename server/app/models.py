from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login 

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, unique=True)
    lastname =db.Column(db.String(64), index=True, unique=True)
    company = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.firstname)  
    
    def __init__(self,firstname,lastname,company,email,password_hash):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.email = email
        self.password_hash = password_hash


    @classmethod
    def authenticate(cls,**kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
    
        if not user or not check_password_hash(user.password_hash,password):
            return None

        print("yes")
        return user
