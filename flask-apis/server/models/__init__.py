from flask_sqlalchemy import SQLAlchemy
import uuid,datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'ems_user'
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    username =  db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(255),nullable=True,default=str("profile.png"))
    permission = db.Column(db.String(255),nullable=True,default=str("customer"))
    created_at = db.Column(db.DateTime,default=datetime.datetime.utcnow())
    update_at = db.Column(db.DateTime,onupdate=datetime.datetime.utcnow())