from flask_sqlalchemy import SQLAlchemy
import uuid,datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    username =  db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.string(255),nullable=True,default=str("profile.png"))
    permission = db.Column(db.string,nullable=True,default=str("customer"))
    createdAt = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    updateAt = db.Column(db.DateTime,onupdate=datetime.datetime.utcnow())