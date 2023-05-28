
from . import db
from flask_login import UserMixin

class Professor(UserMixin,db.Model):
    __tablename__='professores'
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(500), nullable = False)
    email = db.Column(db.String(200),  nullable = False)
    matricula = db.Column(db.String,unique = True, nullable = False)
    password = db.Column(db.String(200))
