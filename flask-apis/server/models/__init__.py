from flask_sqlalchemy import SQLAlchemy
import uuid,datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(150))
    customId=db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    createdAt = db.Column(db.DateTime,default=datetime.timezone.utc)
    updateAt = db.Column(db.DateTime,onupdate=datetime.timezone.utc)